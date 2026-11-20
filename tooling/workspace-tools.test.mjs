import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, realpathSync, rmSync, symlinkSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import test from 'node:test';
import apply from '../lib/startup.js';

function fixture(t) {
  const temp = realpathSync(mkdtempSync(join(tmpdir(), 'ars-workspace-')));
  t.after(() => rmSync(temp, { recursive: true, force: true }));
  const root = join(temp, 'workspace');
  const paper = join(root, 'paper');
  const sibling = join(temp, 'workspace-other');
  mkdirSync(join(paper, 'stage5'), { recursive: true });
  mkdirSync(join(paper, 'phase5_review', 'nested'), { recursive: true });
  mkdirSync(sibling);
  writeFileSync(join(paper, 'stage5', 'final.md'), 'synthetic');
  const tools = new Map();
  let cwd = root;
  apply({
    skills: { register() {} },
    tools: { register(tool) { tools.set(tool.name, tool); } },
    agentPresets: { register() {} },
    workingDirectory: { get() { return cwd; } },
  });
  const exec = { agent: { session: { header: { cwd: root } } } };
  const status = (workspace, context = exec) => tools.get('ars_pipeline_status').execute({ workspace }, context);
  const integrity = (path, context = exec) => tools.get('ars_integrity').execute({ path }, context);
  return { root, paper, sibling, status, integrity, setCwd: (path) => { cwd = path; } };
}

test('both tools support a session-relative and authorized absolute directory', async (t) => {
  const { paper, status, integrity, setCwd } = fixture(t);
  setCwd(paper);
  for (const input of ['.', paper]) {
    const result = await status(input);
    assert.equal(result.workspace, paper);
    assert.deepEqual(result.stages.flatMap(({ files }) => files.map(({ file }) => file)), ['final.md']);
    const report = await integrity(input);
    assert.equal(report.workdir, paper);
    assert.deepEqual(report.phase_dirs['5'], [join(paper, 'phase5_review')]);
  }
});

test('both tools require session authorization and never treat current cwd as a grant', async (t) => {
  const { sibling, status, integrity, setCwd } = fixture(t);
  for (const tool of [status, integrity]) {
    await assert.rejects(tool('.', {}), /no authorized session workspace/);
    await assert.rejects(tool(sibling), /outside the session workspace/);
  }
  setCwd(sibling);
  for (const tool of [status, integrity]) {
    await assert.rejects(tool('.'), /current directory is outside the session workspace/);
  }
});

test('both tools reject linked targets; stat and integrity stay off linked descendants', {
  skip: process.platform === 'win32' && 'Link fixtures need Windows developer mode or elevation',
}, async (t) => {
  const { root, paper, status, integrity } = fixture(t);
  symlinkSync(paper, join(root, 'linked-paper'), 'dir');
  for (const tool of [status, integrity]) {
    await assert.rejects(tool('linked-paper'), /no symbolic links/);
  }
  symlinkSync(join(paper, 'stage5', 'final.md'), join(paper, 'stage5', 'linked.md'));
  const result = await status('paper');
  assert.deepEqual(result.stages[0].files.map(({ file }) => file), ['final.md']);

  symlinkSync(join(paper, 'stage5', 'final.md'), join(paper, 'phase5_review', 'nested', 'linked.md'));
  await assert.rejects(integrity('paper'), /integrity input contains a symbolic link/);
});
