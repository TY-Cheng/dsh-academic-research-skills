#!/usr/bin/env node
// Verify the vendored content against manifest.json and smoke-test the
// registrar. Offline: it never reads the upstream checkout.
import { createHash } from 'node:crypto';
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { join, relative, sep } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = fileURLToPath(new URL('../', import.meta.url));
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
const failures = [];

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

function verifySection(name, root, expectedFiles) {
  if (!existsSync(root)) {
    failures.push(`${name}: missing root ${relative(ROOT, root)}`);
    return;
  }
  const expected = new Map(expectedFiles.map((file) => [file.path, file.sha256]));
  const actual = walkFiles(root).map((path) => relative(ROOT, path).split(sep).join('/'));
  const actualSet = new Set(actual);
  const local = [];
  for (const [path, hash] of expected) {
    if (!actualSet.has(path)) {
      local.push(`missing ${path}`);
    } else if (sha256(join(ROOT, path)) !== hash) {
      local.push(`modified ${path}`);
    }
  }
  for (const path of actual) {
    if (!expected.has(path)) local.push(`extra ${path}`);
  }
  if (local.length) {
    failures.push(...local.map((line) => `${name}: ${line}`));
  } else {
    console.log(`verify: ${name} ${expected.size} files OK`);
  }
}

function verifyFiles(name, expectedFiles) {
  const local = [];
  for (const file of expectedFiles) {
    const path = join(ROOT, file.path);
    if (!existsSync(path)) local.push(`missing ${file.path}`);
    else if (sha256(path) !== file.sha256) local.push(`modified ${file.path}`);
  }
  if (local.length) {
    failures.push(...local.map((line) => `${name}: ${line}`));
  } else {
    console.log(`verify: ${name} ${expectedFiles.length} files OK`);
  }
}

const manifest = JSON.parse(readFileSync(join(ROOT, 'manifest.json'), 'utf8'));
if (manifest.schemaVersion !== 2) {
  console.error(`unsupported manifest schemaVersion: ${manifest.schemaVersion}`);
  process.exit(1);
}
const { skills, core, commands } = manifest.vendored;
verifySection('skills', join(ROOT, 'skills'), skills.files);
for (const dir of core.directories) {
  verifySection(`core/${dir.destination}`, join(ROOT, dir.destination), dir.files);
}
verifyFiles('core/root-files', core.files);
verifySection('commands', join(ROOT, 'commands'), commands.files);

if (failures.length) {
  console.error('vendored content drift:');
  for (const failure of failures) console.error(`  ${failure}`);
  console.error('run `npm run sync -- <upstream-checkout>` and review the diff');
  process.exit(1);
}

const { default: apply } = await import(pathToFileURL(join(ROOT, 'lib', 'startup.js')).href);
const registered = [];
apply({ skills: { register: (skill) => registered.push(skill) } });
const expectedRegistrations = skills.directories.length + commands.files.length;
if (registered.length !== expectedRegistrations) {
  console.error(
    `registrar: expected ${expectedRegistrations} registrations, got ${registered.length}`,
  );
  process.exit(1);
}
console.log(`registrar: ${registered.length} registrations OK`);
