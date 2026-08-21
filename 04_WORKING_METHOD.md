# Working Method

## Purpose
Define how the project is managed and how AI execution is controlled.

## Roles
### Human Project Owners
The founder and ChatGPT jointly direct strategy, requirements, prioritization, and review.

### Execution Agent
Antigravity CLI using Gemini 3.1 Pro performs implementation and document work according to explicit sprint instructions.

### GitHub
GitHub is the version-controlled source of project history.

## Required Agent Behavior
The execution agent must:
1. Read `README.md` and all relevant project documents before editing.
2. Preserve confirmed decisions.
3. Avoid assumptions when facts are missing.
4. Work in the requested document order.
5. Complete one document, validate it against related documents, then proceed to the next.
6. Run a consistency audit after the full sprint.
7. Produce an audit report.
8. Commit completed work with meaningful commit messages.
9. Never push unless explicitly instructed.
10. Never silently broaden scope.

## Definition of Done
A sprint is complete only when:
- requested documents are completed,
- cross-document consistency is checked,
- contradictions are listed or resolved,
- unsupported assumptions are identified,
- an audit report is written,
- changes are committed.

## Related Documents
- 02_PROJECT_PRINCIPLES.md
- ROADMAP.md
- DECISIONS.md
