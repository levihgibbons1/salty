# Local development

## Prerequisites

Git and Python 3.12–3.14 with pip and venv. CI checks Python 3.12 and 3.14. No Docker, Node, school credentials, paid AI account, or cloud database is required for this scaffold. Internet access is needed to install dependencies.

## First run

```sh
git clone https://github.com/levihgibbons1/salty.git
cd salty
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/dev.py setup
python manage.py runserver 127.0.0.1:8000
```

Windows PowerShell: use `py -3.14 -m venv .venv` and `.venv\Scripts\Activate.ps1` instead of the first two Python/environment commands. If activation is unavailable, invoke `.venv\Scripts\python.exe` directly for each command. On macOS/Linux the equivalent is `.venv/bin/python`.

Open `http://127.0.0.1:8000/` for a plain-text scaffold status, or `http://127.0.0.1:8000/health/` for `{"status":"ok"}`. This is not the future SALTY dashboard. Stop with Ctrl+C. Use loopback only; this development server is not a deployment.

## Configuration and storage

Setup creates ignored `.local/settings.json` with a generated local secret, `.local/salty.sqlite3`, and `.local/files/`. It preserves existing configuration and applies pending Django migrations. `config.example.json` documents the required shape without containing credentials. The application refuses missing/invalid configuration and any environment other than development/test.

No environment-variable secrets or `.env` loader are implemented. Do not put real school data into this scaffold. Files are not exposed by URL; future downloads require authorization. The only current tables are framework migration/content-type metadata. Person and academic models arrive in later tasks; Django’s default user model has deliberately not been enabled before M1-02 selects the identity model.

## Commands

| Command | Effect |
| --- | --- |
| `python scripts/dev.py setup` | Create missing local configuration/storage and migrate the database |
| `python manage.py runserver 127.0.0.1:8000` | Start local HTTP service |
| `python scripts/dev.py check` | Lint, format check, docs, Django checks, migration drift check, tests |
| `python -m ruff format .` | Format Python files |
| `python manage.py migrate` | Apply pending migrations |
| `python scripts/dev.py reset --confirm` | Delete and recreate only the local SQLite database; preserve configuration and stored files |

Stop the server before reset. Reset destroys local database records and can orphan preserved files; it is a development recovery command, not a production migration tool. It does not seed academic data. Without `--confirm` it refuses deletion.

## Troubleshooting

- Missing/invalid configuration: run setup. If the existing JSON is invalid, correct its shape using the example; setup never silently overwrites it.
- Port occupied: use `127.0.0.1:8001` instead.
- Health returns 503: run migrations and inspect local service output. The endpoint deliberately omits database error details.
- Installation certificate error: configure Python with your OS/organization’s trusted CA bundle. Never disable certificate verification.

Dependencies are exactly pinned in requirements.txt, including Windows timezone data. Review updates and run the full checks. This is a Python source application: there is no frontend build or static type-checking stage yet; Ruff, Django checks, and tests are the current verification tools.
