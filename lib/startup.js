// dsh-academic-research-skills — startup plugin.
//
// Registers the ported Academic Research Skills (ARS) suite into ctx.skills:
//   - 5 vendored model-invocable skills
//   - 2 native DSH team skills (ars-team, ars-pipeline-team)
//   - 16 user-invocable commands: /ars-3w ... /ars-unmark-read
//   - 5 native tools (ars_search, ars_lookup, ars_integrity, ars_pipeline_status,
//     ars_manifest) when ctx.tools is mounted
//   - the ARS Team agent preset when ctx.agentPresets is mounted
//
// Dependency-free by design (no runtime imports beyond Node's standard library),
// so the package installs offline and the loader has nothing extra to resolve.
//
// Skill bodies are read from the package's own skills/ and commands/
// directories at mount time, and each registration carries a directory
// resourceBase so relative references (references/, agents/, templates/,
// examples/) resolve against the bundled files.
//
// The full ARS core is also vendored at the package root (scripts/, shared/,
// agents/, MODE_REGISTRY.md). A short note is prepended to every registered
// body so the agent resolves those root-relative paths against the package,
// not the paper project's working directory.
import { readFileSync, readdirSync, existsSync, statSync } from 'node:fs';
import { join, dirname, isAbsolute } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';

const execFileAsync = promisify(execFile);

const PACKAGE_ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const ARS_ROOT_NOTE =
  `> **ARS package root:** \`${PACKAGE_ROOT}\`\n` +
  `> Shared ARS tooling (\`scripts/\`, \`shared/\`, \`agents/\`, \`MODE_REGISTRY.md\`) lives there, not in the paper project's working directory. Resolve root-relative paths against it; paths inside this skill's own bundle (for example \`sr-screener/scripts/\`) stay relative to the skill. \`DSH_ARS_ROOT\` is set to the same root.\n\n`;

const SKILL_DIRS = [
  'skills/deep-research',
  'skills/academic-paper',
  'skills/academic-paper-reviewer',
  'skills/academic-pipeline',
  'skills/sr-screener',
  'native/skills/ars-team',
  'native/skills/ars-pipeline-team',
];

const NAME_RE = /^[a-z0-9]+(-[a-z0-9]+)*$/;

/**
 * Minimal frontmatter reader: line-based `key: value` extraction sufficient
 * for the ARS skill files (single-line name/description, nested metadata
 * blocks skipped). No YAML dependency.
 */
function parseFrontmatter(text) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---/.exec(text);
  if (!match) return null;
  const fields = {};
  for (const line of match[1].split(/\r?\n/)) {
    if (!line || /^\s/.test(line) || line.trim().startsWith('#')) continue;
    const idx = line.indexOf(':');
    if (idx <= 0) continue;
    const key = line.slice(0, idx).trim();
    if (fields[key] !== undefined) continue; // first occurrence wins
    let value = line.slice(idx + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    fields[key] = value;
  }
  return fields;
}

/**
 * Load one skill bundle (<dir>/SKILL.md) from the package root.
 * @param {string} rel - package-relative directory, e.g. 'skills/deep-research'.
 * @returns {{ name: string, description: string, content: string,
 *             resourceBase: { kind: 'directory', path: string } } | null}
 */
function loadSkill(rel) {
  const skillDir = join(PACKAGE_ROOT, rel);
  const file = join(skillDir, 'SKILL.md');
  if (!existsSync(file) || !statSync(file).isFile()) return null;
  const text = readFileSync(file, 'utf8');
  const fm = parseFrontmatter(text);
  if (!fm) return null;
  const name = fm.name;
  const description = fm.description;
  if (typeof name !== 'string' || !NAME_RE.test(name)) return null;
  if (typeof description !== 'string' || description.length === 0) return null;
  const content = text.slice(text.indexOf('---', 3) + 3).replace(/^\r?\n/, '');
  return {
    name,
    description,
    content,
    resourceBase: { kind: 'directory', path: skillDir },
  };
}

function mapOpenAlexWork(work) {
  return {
    id: work?.id ?? null,
    doi: work?.doi ?? null,
    title: work?.title ?? null,
    year: work?.publication_year ?? null,
    venue: work?.primary_location?.source?.display_name ?? null,
    authors: (work?.authorships ?? [])
      .map((authorship) => authorship?.author?.display_name)
      .filter(Boolean),
    cited_by_count: work?.cited_by_count ?? null,
    type: work?.type ?? null,
  };
}

const NATIVE_TOOL_DEFS = [
  {
    name: 'ars_search',
    description:
      'Search OpenAlex for scholarly works and return compact metadata (DOI, title, year, venue, authors, citations). Read-only; no Python or shell.',
    parameters: {
      type: 'object',
      properties: {
        query: { type: 'string', description: 'Full-text search query.' },
        limit: {
          type: 'integer',
          minimum: 1,
          maximum: 25,
          default: 10,
          description: 'Maximum records to return (1-25).',
        },
      },
      required: ['query'],
      additionalProperties: false,
    },
    output: {
      schema: {
        type: 'object',
        properties: {
          query: { type: 'string' },
          count: { type: 'integer' },
          records: {
            type: 'array',
            items: { type: 'object', additionalProperties: true },
          },
        },
        required: ['query', 'count', 'records'],
        additionalProperties: false,
      },
      render(_args, value) {
        return [{ type: 'text', text: JSON.stringify(value, null, 2) }];
      },
    },
    timeoutMs: 30_000,
    isConcurrencySafe: () => true,
    async execute(args) {
      const query = typeof args?.query === 'string' ? args.query.trim() : '';
      if (!query) throw new Error('ars_search: query is required');
      const limit = Math.min(Math.max(Number(args?.limit) || 10, 1), 25);
      const url = new URL('https://api.openalex.org/works');
      url.searchParams.set('search', query);
      url.searchParams.set('per-page', String(limit));
      url.searchParams.set(
        'select',
        'id,doi,title,publication_year,authorships,primary_location,cited_by_count,type',
      );
      const response = await fetch(url, {
        headers: {
          Accept: 'application/json',
          'User-Agent': 'dsh-academic-research-skills/0.4.2',
        },
        signal: AbortSignal.timeout(25_000),
      });
      if (!response.ok) throw new Error(`ars_search: OpenAlex HTTP ${response.status}`);
      const data = await response.json();
      const records = (data?.results ?? []).map(mapOpenAlexWork);
      return { query, count: records.length, records };
    },
  },
  {
    name: 'ars_lookup',
    description:
      'Look up one scholarly work by DOI via OpenAlex or Crossref and return compact metadata. Read-only; no Python or shell.',
    parameters: {
      type: 'object',
      properties: {
        doi: {
          type: 'string',
          description: 'DOI, with or without the https://doi.org/ prefix.',
        },
        source: {
          type: 'string',
          enum: ['openalex', 'crossref'],
          default: 'openalex',
          description: 'Metadata source.',
        },
      },
      required: ['doi'],
      additionalProperties: false,
    },
    output: {
      schema: { type: 'object', additionalProperties: true },
      render(_args, value) {
        return [{ type: 'text', text: JSON.stringify(value, null, 2) }];
      },
    },
    timeoutMs: 30_000,
    isConcurrencySafe: () => true,
    async execute(args) {
      const doi = String(args?.doi ?? '')
        .replace(/^https?:\/\/doi\.org\//i, '')
        .trim();
      if (!doi) throw new Error('ars_lookup: doi is required');
      const source = args?.source === 'crossref' ? 'crossref' : 'openalex';
      if (source === 'crossref') {
        const response = await fetch(
          `https://api.crossref.org/works/${encodeURIComponent(doi)}`,
          {
            headers: {
              Accept: 'application/json',
              'User-Agent': 'dsh-academic-research-skills/0.4.2',
            },
            signal: AbortSignal.timeout(25_000),
          },
        );
        if (!response.ok) throw new Error(`ars_lookup: Crossref HTTP ${response.status}`);
        const message = (await response.json())?.message ?? {};
        return {
          source,
          doi: message.DOI ?? doi,
          title: message.title?.[0] ?? null,
          year: message.issued?.['date-parts']?.[0]?.[0] ?? null,
          venue: message['container-title']?.[0] ?? null,
          authors: (message.author ?? [])
            .map((author) => [author.given, author.family].filter(Boolean).join(' '))
            .filter(Boolean),
          cited_by_count: message['is-referenced-by-count'] ?? null,
          type: message.type ?? null,
        };
      }
      const response = await fetch(
        `https://api.openalex.org/works/https://doi.org/${encodeURIComponent(doi)}`,
        {
          headers: {
            Accept: 'application/json',
            'User-Agent': 'dsh-academic-research-skills/0.4.2',
          },
          signal: AbortSignal.timeout(25_000),
        },
      );
      if (!response.ok) throw new Error(`ars_lookup: OpenAlex HTTP ${response.status}`);
      return { source, ...mapOpenAlexWork(await response.json()) };
    },
  },
  {
    name: 'ars_integrity',
    description:
      'Run the vendored ARS pipeline integrity checker (scripts/check_pipeline_integrity.py --json) on a workspace and return its JSON findings. Read-only; the checker is executed without a shell.',
    parameters: {
      type: 'object',
      properties: {
        path: {
          type: 'string',
          description: 'Workspace or paper directory to check.',
        },
      },
      required: ['path'],
      additionalProperties: false,
    },
    output: {
      schema: { type: 'object', additionalProperties: true },
      render(_args, value) {
        return [{ type: 'text', text: JSON.stringify(value, null, 2) }];
      },
    },
    timeoutMs: 60_000,
    isConcurrencySafe: () => true,
    async execute(args) {
      const target = typeof args?.path === 'string' ? args.path.trim() : '';
      if (!target) throw new Error('ars_integrity: path is required');
      const script = join(PACKAGE_ROOT, 'scripts/check_pipeline_integrity.py');
      if (!existsSync(script)) throw new Error('ars_integrity: checker script not found');
      const venvPython = join(PACKAGE_ROOT, '.venv/bin/python');
      const python = process.env.DSH_ARS_PYTHON || (existsSync(venvPython) ? venvPython : 'python3');
      const { stdout } = await execFileAsync(python, [script, '--json', target], {
        cwd: PACKAGE_ROOT,
        timeout: 50_000,
        maxBuffer: 10 * 1024 * 1024,
      });
      try {
        return { checker: 'check_pipeline_integrity.py', ...JSON.parse(stdout) };
      } catch {
        return { checker: 'check_pipeline_integrity.py', raw: stdout };
      }
    },
  },
  {
    name: 'ars_pipeline_status',
    description:
      'Summarize ARS pipeline-stage artifacts in a workspace: stage directories, Markdown files, and modification times. Read-only.',
    parameters: {
      type: 'object',
      properties: {
        workspace: {
          type: 'string',
          description: 'Pipeline workspace, e.g. examples/dsh/iv-surface-review.',
        },
      },
      required: ['workspace'],
      additionalProperties: false,
    },
    output: {
      schema: { type: 'object', additionalProperties: true },
      render(_args, value) {
        return [{ type: 'text', text: JSON.stringify(value, null, 2) }];
      },
    },
    timeoutMs: 15_000,
    isConcurrencySafe: () => true,
    execute(args) {
      const workspace = typeof args?.workspace === 'string' ? args.workspace.trim() : '';
      if (!workspace) throw new Error('ars_pipeline_status: workspace is required');
      const root = isAbsolute(workspace) ? workspace : join(process.cwd(), workspace);
      if (!existsSync(root) || !statSync(root).isDirectory()) {
        throw new Error(`ars_pipeline_status: workspace not found: ${workspace}`);
      }
      const stages = [];
      for (const entry of readdirSync(root)) {
        const full = join(root, entry);
        if (!statSync(full).isDirectory()) continue;
        if (!/^(stage|paper|review)/i.test(entry)) continue;
        const files = readdirSync(full)
          .filter((file) => file.endsWith('.md'))
          .map((file) => ({
            file,
            mtime: statSync(join(full, file)).mtime.toISOString(),
          }));
        stages.push({ dir: entry, files });
      }
      return { workspace, stages };
    },
  },
  {
    name: 'ars_manifest',
    description:
      'Read the vendored ARS manifest: pinned upstream repository/commit, vendored content counts, and the not-vendored boundary. Read-only.',
    parameters: {
      type: 'object',
      properties: {},
      additionalProperties: false,
    },
    output: {
      schema: { type: 'object', additionalProperties: true },
      render(_args, value) {
        return [{ type: 'text', text: JSON.stringify(value, null, 2) }];
      },
    },
    timeoutMs: 5_000,
    isConcurrencySafe: () => true,
    execute() {
      const manifestPath = join(PACKAGE_ROOT, 'manifest.json');
      if (!existsSync(manifestPath)) throw new Error('ars_manifest: manifest.json not found');
      const manifest = JSON.parse(readFileSync(manifestPath, 'utf8'));
      const coreDirs = manifest.vendored?.core?.directories ?? [];
      const coreDirFiles = coreDirs.reduce((total, dir) => total + (dir.files?.length ?? 0), 0);
      const coreRootFiles = manifest.vendored?.core?.files?.length ?? 0;
      const skillFiles = manifest.vendored?.skills?.files?.length ?? 0;
      return {
        schemaVersion: manifest.schemaVersion,
        upstream: manifest.upstream,
        counts: {
          skills: skillFiles,
          coreDirectories: coreDirFiles,
          coreRootFiles,
          vendoredTotal: skillFiles + coreDirFiles + coreRootFiles,
          commands: manifest.vendored?.commands?.files?.length ?? 0,
        },
        notVendored: manifest.notVendored ?? [],
      };
    },
  },
];

const ARS_PRESET = {
  id: 'ars-team',
  name: 'ARS Team',
  description:
    'Academic Research Skills with the native ars-team five-seat panel, Team board, and citation tools.',
  order: 10,
  plugins: [{ id: 'ars-skills', name: 'dsh-academic-research-skills/startup' }],
};

function registerNativeTools(ctx) {
  for (const definition of NATIVE_TOOL_DEFS) ctx.tools.register(definition);
  console.log(
    `[dsh-academic-research-skills] registered ${NATIVE_TOOL_DEFS.length} native tools`,
  );
}

/**
 * Cordis plugin body. `ctx.skills` is injected by the bundle patch row
 * (`inject: [skills]`); the guard keeps the module safe if mounted without it.
 */
export default function apply(ctx) {
  if (!ctx?.skills) {
    console.warn('[dsh-academic-research-skills] ctx.skills unavailable — skills not registered');
    return;
  }

  process.env.DSH_ARS_ROOT ??= PACKAGE_ROOT;

  let registered = 0;
  for (const rel of SKILL_DIRS) {
    const skill = loadSkill(rel);
    if (!skill) {
      console.warn(`[dsh-academic-research-skills] failed to load ${rel}`);
      continue;
    }
    ctx.skills.register({ ...skill, content: ARS_ROOT_NOTE + skill.content, source: 'runtime' });
    registered += 1;
  }

  const commandsDir = join(PACKAGE_ROOT, 'commands');
  if (existsSync(commandsDir)) {
    for (const entry of readdirSync(commandsDir)) {
      if (!statSync(join(commandsDir, entry)).isDirectory()) continue;
      const skill = loadSkill(`commands/${entry}`);
      if (!skill) continue;
      ctx.skills.register({
        ...skill,
        content: ARS_ROOT_NOTE + skill.content,
        source: 'runtime',
        invocation: { modelInvocable: false, userInvocable: true },
      });
      registered += 1;
    }
  }

  if (ctx.tools) {
    registerNativeTools(ctx);
  } else {
    console.warn(
      '[dsh-academic-research-skills] ctx.tools unavailable — native tools not registered',
    );
  }

  if (ctx.agentPresets) {
    void Promise.resolve(ctx.agentPresets.register(ARS_PRESET)).catch((error) => {
      console.warn(`[dsh-academic-research-skills] failed to register ARS Team preset: ${error}`);
    });
    console.log('[dsh-academic-research-skills] registered ARS Team preset');
  } else {
    console.warn(
      '[dsh-academic-research-skills] ctx.agentPresets unavailable — ARS Team preset not registered',
    );
  }

  console.log(
    `[dsh-academic-research-skills] registered ${registered} skills (ARS root: ${PACKAGE_ROOT})`,
  );
}
