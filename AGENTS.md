# Repository Guidelines

## Project Structure & Module Organization
This repository is currently documentation-first. All tracked project content lives in [`docs/`](/home/monkey/apps/SBAI/docs):

- [`docs/SPEC.md`](/home/monkey/apps/SBAI/docs/SPEC.md): product and file-level specification for the SBAI skill.
- [`docs/Questionnaire.md`](/home/monkey/apps/SBAI/docs/Questionnaire.md): question set and scoring rules.
- [`docs/Types.md`](/home/monkey/apps/SBAI/docs/Types.md): the 24 personality definitions.

When implementation starts, keep generated code and data aligned with the structure described in `docs/SPEC.md` (`SKILL.md`, `questionnaire.json`, `types.json`, `combinations.json`, `scoring.py`, `generate_result.py`, `template.html`, `assets/`).

## Build, Test, and Development Commands
There is no runnable app or test suite in the repository yet. For now, contributors mainly review and edit Markdown docs.

- `rg --files docs`: list documentation files quickly.
- `sed -n '1,120p' docs/SPEC.md`: inspect a document section before editing.
- `markdownlint docs/**/*.md`: optional, if available locally, to catch heading and spacing issues.

Add project-specific build and test commands here as soon as implementation files are introduced.

## Coding Style & Naming Conventions
Use concise Markdown with short sections, consistent heading levels, and tight bullet lists. Keep terminology consistent across files: use the same type codes, question IDs, and file names everywhere.

For planned data files, prefer:

- snake_case for JSON and Python file names (`generate_result.py`)
- stable uppercase type codes (`YYDS`, `PUA`)
- clear, deterministic keys such as `primary_type`, `secondary_type`, and `combo_name`

## Testing Guidelines
Until code exists, review changes for cross-file consistency rather than runtime behavior. Verify that:

- question text matches its scoring map
- type codes are spelled identically in every document
- planned file names in docs match the spec exactly

If Python scripts are added later, introduce `pytest` tests under `tests/` and document the command here.

## Commit & Pull Request Guidelines
The repository has no commit history yet, so there is no established convention to copy. Start with short, imperative commit subjects such as `Add SBAI contributor guide` or `Refine questionnaire scoring notes`.

Pull requests should include a brief summary, the files changed, and any spec decisions or terminology changes that affect other docs. Include screenshots only if a rendered HTML result page is added later.
