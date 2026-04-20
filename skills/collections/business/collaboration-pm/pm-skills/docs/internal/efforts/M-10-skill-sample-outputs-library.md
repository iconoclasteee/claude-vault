# M-10 - Skill sample outputs library

Status: Closed-aligned (v2.5.0 gate closed; mirror parity applied)  
Owner: Maintainers  
Last updated: 2026-03-02

id: M-10
kind: content
release_target: v2.5.0
repo_scope: both
github_issue: TBD
local_working_path: _NOTES/efforts/active/M-10-skill-sample-library/

## Objective

Add a tracked sample-output collection for skills in `library/skill-output-samples/<skill-name>/` and keep pm-skills / pm-skills-mcp automation and parity aligned.

## Dependencies

1. Architecture-first behavior (`M-09`, `F-02`, `F-04`) is stable enough to produce canonical samples.
2. `D12` policy is locked and linked across release bundle/checklist artifacts.
3. Release-note/changelog structure is ready for final shipped manifest claims.

## Decision Mapping

1. Primary: `D12` (exactly 3 samples per shipped skill with canonical manifest).
2. Supporting: `D6` (if sample behavior reflects breaking MCP changes), `D11` (contract signaling).

## Acceptance Criteria

1. Sample library artifacts exist in canonical location and map to shipped behavior.
2. `library/skill-output-samples/manifest.v2.5.0.json` links each shipped skill to exactly 3 expected sample files.
3. Release claims, checklist, and test matrix reference the same locked manifest.
4. Current inclusion baseline (`f02-included`) is 25 skills and 75 sample files.

## Release Gates

1. Release cut is blocked on unresolved manifest ambiguity or failed 3-per-skill coverage checks.
2. Gate status: closed (`manifest.v2.5.0.json` is locked at `f02-included`; checklist M-10 evidence rerun timestamp `2026-03-02 17:57 PT`).
3. `github_issue` remains `TBD` (governance follow-up; not blocking v2.5.0 cut).

## Closure Alignment Evidence

1. `docs/internal/release-planning/checklist_v2.5.0.md` marks `M-10` gate closed with explicit matrix evidence.
2. `_NOTES/efforts/active/M-10-skill-sample-library/m-10_reviewed-by-gpt-5.3.md` includes defect breakdown and closure recommendation.
3. Latest matrix rerun passed (`validate-commands`, `lint-skills-frontmatter`, `validate-mcp-sync`, `embed/build/test`) on `2026-03-02 17:57 PT`.

## Canonical links

1. docs/internal/backlog-canonical.md
2. docs/internal/release-planning/checklist_v2.5.0.md
3. docs/internal/release-planning/Release_v2.2_to_v2.5_execution-plan.md
4. docs/guides/validate-mcp-sync.md
5. _NOTES/delivery-plan/releases/v2.5.0/RELEASE_BUNDLE_v2.5.0.md
