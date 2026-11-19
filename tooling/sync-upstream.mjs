#!/usr/bin/env node
// Sync vendored Academic Research Skills content from an upstream checkout.
//
//   node tooling/sync-upstream.mjs <upstream-repo-path>
//
// The upstream checkout must be clean. This copies the five skill directories
// plus the shared ARS core (scripts/, shared/, agents/, MODE_REGISTRY.md and
// friends) byte-for-byte, regenerates the DSH command wrappers, and rewrites
// manifest.json with the upstream pin and per-file SHA-256 hashes.
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import {
  chmodSync,
  cpSync,
  existsSync,
  readFileSync,
  readdirSync,
  rmSync,
  statSync,
  writeFileSync,
} from 'node:fs';
import { basename, join, relative, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = fileURLToPath(new URL('../', import.meta.url));
const MANIFEST = join(ROOT, 'manifest.json');
const UPSTREAM_REPOSITORY = 'https://github.com/Imbad0202/academic-research-skills';
const SKILLS = [
  'deep-research',
  'academic-paper',
  'academic-paper-reviewer',
  'academic-pipeline',
  'sr-screener',
];
// Core ARS directories, vendored byte-for-byte from the upstream root.
const CORE_DIRECTORIES = ['scripts', 'shared', 'agents'];
// Core root files referenced by the skills/commands.
const CORE_FILES = [
  'MODE_REGISTRY.md',
  'THIRD_PARTY.md',
  'requirements-dev.txt',
  'requirements-pdf-content-classifier.txt',
];
const IGNORED = new Set([
  '.git',
  '.DS_Store',
  'Thumbs.db',
  '__pycache__',
  '.pytest_cache',
  '.mypy_cache',
  '.ruff_cache',
  '.venv',
]);

const upstream = resolve(process.argv[2] ?? '');
if (!process.argv[2]) {
  console.error('usage: node tooling/sync-upstream.mjs <upstream-repo-path>');
  process.exit(1);
}
if (!existsSync(join(upstream, 'commands'))) {
  console.error(`not an ARS checkout: ${upstream}`);
  process.exit(1);
}
for (const skill of SKILLS) {
  if (!existsSync(join(upstream, skill, 'SKILL.md'))) {
    console.error(`missing upstream skill: ${skill}`);
    process.exit(1);
  }
}
for (const dir of CORE_DIRECTORIES) {
  if (!existsSync(join(upstream, dir))) {
    console.error(`missing upstream core directory: ${dir}`);
    process.exit(1);
  }
}
for (const file of CORE_FILES) {
  if (!existsSync(join(upstream, file))) {
    console.error(`missing upstream core file: ${file}`);
    process.exit(1);
  }
}

function git(args) {
  return execFileSync('git', ['-C', upstream, ...args], { encoding: 'utf8' }).trim();
}

const dirty = git(['status', '--porcelain']);
if (dirty) {
  console.error('upstream checkout is dirty; commit or stash first:');
  console.error(dirty);
  process.exit(1);
}

const commit = git(['rev-parse', 'HEAD']);
const describe = git(['describe', '--tags', '--always']);
let tag = '';
try {
  tag = git(['describe', '--tags', '--abbrev=0']);
} catch {
  // A checkout without tags is allowed; the commit hash is still pinned.
}
const version = tag.replace(/^v/, '') || 'unknown';

function ignored(name) {
  return IGNORED.has(name) || name.endsWith('.pyc');
}

function walkFiles(root) {
  const files = [];
  const visit = (dir) => {
    for (const entry of readdirSync(dir, { withFileTypes: true })) {
      if (ignored(entry.name)) continue;
      const path = join(dir, entry.name);
      if (entry.isDirectory()) visit(path);
      else if (entry.isFile()) files.push(path);
    }
  };
  visit(root);
  return files.sort();
}

function sha256(file) {
  return createHash('sha256').update(readFileSync(file)).digest('hex');
}

function copyTree(src, dest) {
  rmSync(dest, { recursive: true, force: true });
  cpSync(src, dest, {
    recursive: true,
    filter: (path) => !ignored(basename(path)),
  });
  // cpSync does not promise to preserve the source mode on every platform.
  for (const file of walkFiles(dest)) {
    chmodSync(file, statSync(join(src, relative(dest, file))).mode);
  }
}

function fileEntries(root) {
  return walkFiles(root).map((path) => ({
    path: relative(ROOT, path).split(sep).join('/'),
    sha256: sha256(path),
  }));
}

// 1. Vendored skills: byte-identical copies of the upstream root directories.
const skillsRoot = join(ROOT, 'skills');
rmSync(skillsRoot, { recursive: true, force: true });
for (const skill of SKILLS) {
  copyTree(join(upstream, skill), join(skillsRoot, skill));
}

// 2. Vendored core: shared Python tooling, contracts, and root agents.
for (const dir of CORE_DIRECTORIES) {
  copyTree(join(upstream, dir), join(ROOT, dir));
}
for (const file of CORE_FILES) {
  cpSync(join(upstream, file), join(ROOT, file));
  chmodSync(join(ROOT, file), statSync(join(upstream, file)).mode);
}

// Warn if upstream grows a skill that lib/startup.js does not register.
const upstreamSkills = readdirSync(upstream, { withFileTypes: true })
  .filter((entry) => entry.isDirectory() && existsSync(join(upstream, entry.name, 'SKILL.md')))
  .map((entry) => entry.name)
  .sort();
const unregistered = upstreamSkills.filter((name) => !SKILLS.includes(name));
if (unregistered.length) {
  console.warn(`warning: upstream skills not registered in lib/startup.js: ${unregistered.join(', ')}`);
}

// 3. DSH command wrappers: generated, never copied from upstream unchanged.
rmSync(join(ROOT, 'commands'), { recursive: true, force: true });
execFileSync(process.execPath, [join(ROOT, 'tooling', 'regenerate-commands.mjs'), upstream], {
  cwd: ROOT,
  stdio: 'inherit',
});

// 4. Manifest: pin plus hashes of every vendored and generated file.
const sourceCommands = readdirSync(join(upstream, 'commands'))
  .filter((file) => /^ars-.*\.md$/.test(file))
  .sort()
  .map((file) => ({
    path: `commands/${file}`,
    sha256: sha256(join(upstream, 'commands', file)),
  }));

const manifest = {
  schemaVersion: 2,
  upstream: {
    repository: UPSTREAM_REPOSITORY,
    version,
    tag: tag || null,
    commit,
    describe,
    license: 'CC-BY-NC-4.0',
  },
  maintainer: 'TY-Cheng',
  syncPolicy: 'SYNC_POLICY.md',
  syncedAt: new Date().toISOString(),
  vendored: {
    skills: {
      source: 'upstream root skill directories',
      destination: 'skills',
      directories: SKILLS,
      files: fileEntries(skillsRoot),
    },
    core: {
      source: 'upstream root core directories and files',
      directories: CORE_DIRECTORIES.map((dir) => ({
        source: `upstream ${dir}/`,
        destination: dir,
        files: fileEntries(join(ROOT, dir)),
      })),
      files: CORE_FILES.map((file) => ({
        source: `upstream ${file}`,
        path: file,
        sha256: sha256(join(ROOT, file)),
      })),
    },
    commands: {
      source: 'upstream commands/ars-*.md',
      destination: 'commands',
      generatedBy: 'tooling/regenerate-commands.mjs',
      sourceFiles: sourceCommands,
      files: fileEntries(join(ROOT, 'commands')),
    },
  },
  notVendored: {
    note: 'Upstream paths not included in this distribution; see SYNC_POLICY.md.',
    paths: [
      'audits',
      'docs',
      'evals',
      'examples',
      'hooks',
      'pi',
      'plugin-evals',
      'plugin-evals-citation-check',
      'plugin-evals-citation-locale',
      'CITATION.cff',
      'CHANGELOG.md',
      'CONTRIBUTING.md',
      'GOVERNANCE.md',
      'LICENSE',
      'NOTICE.md',
      'POSITIONING.md',
      'QUICKSTART.md',
      'README*.md',
      'SECURITY.md',
      'package.json',
      'pyproject.toml',
    ],
  },
};

writeFileSync(MANIFEST, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');

console.log(`synced ARS ${version} (${describe}) from ${upstream}`);
console.log(`skills: ${SKILLS.length} dirs, ${manifest.vendored.skills.files.length} files`);
console.log(
  `core: ${CORE_DIRECTORIES.join(', ')} + ${CORE_FILES.length} root files, ` +
    `${manifest.vendored.core.directories.reduce((n, dir) => n + dir.files.length, 0) + CORE_FILES.length} files`,
);
console.log(
  `commands: ${sourceCommands.length} upstream files -> ${manifest.vendored.commands.files.length} generated files`,
);
console.log(`manifest: ${relative(ROOT, MANIFEST)}`);
console.log('next: npm run verify');
