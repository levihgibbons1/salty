# Contributing to SALTY

## Setup today

Requirements: Git and Python 3.10+. An AI tool is optional.

```sh
git clone https://github.com/levihgibbons1/salty.git
cd salty
python3 scripts/check_docs.py
```

There is no application to start yet. Application setup and fixture commands must be added with the implementation, not represented as already working.

Read [AGENTS.md](AGENTS.md) and [the milestone](docs/milestone-1.md). If using an assistant, ask it to read those files explicitly. CLAUDE.md and GEMINI.md are entry points to the same instructions; other tools can read AGENTS.md directly.

## Choose work

Open a task issue using the template. Reference a milestone item, define the expected behavior and how it will be verified, and coordinate ownership before starting overlapping work. The first implementation task is M1-01: choose and scaffold the development stack.

A useful agent prompt is: “Read AGENTS.md and the milestone. Implement issue NUMBER within its scope, run relevant checks, and report what works and what remains unfinished.”

## Submit work

1. Create a descriptive branch, such as `feat/academic-import` or `docs/setup`.
2. Make the smallest complete change that satisfies the task.
3. Add behavior-focused tests for imports, authorization, and persistence as those features arrive.
4. Run documented checks and update setup instructions when commands change.
5. Open a pull request with evidence and limitations. A maintainer reviews before merge.

Use preview environments with fictional data once hosting exists. Maintainers should configure required checks and branch protection when repository settings and the development workflow are ready. Those protections are not established by this document.

## School information

Do not place private records in issues, screenshots, logs, or pull requests. Use sample data. Report suspected exposure privately to a repository maintainer rather than reproducing sensitive content in a public issue.
