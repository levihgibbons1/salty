"""Cross-platform local setup and checks. No shell activation required internally."""

import argparse
import json
import secrets
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local"


def run(*args):
    subprocess.run([sys.executable, *args], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["setup", "check", "reset"])
    parser.add_argument("--confirm", action="store_true", help="Confirm deletion of local database")
    args = parser.parse_args()
    if args.command == "check":
        run("-m", "ruff", "check", ".")
        run("-m", "ruff", "format", "--check", ".")
        run("scripts/check_docs.py")
        run("manage.py", "check")
        run("manage.py", "makemigrations", "--check", "--dry-run")
        run("manage.py", "test")
        return
    # Never follow a replaced storage directory when creating or deleting local files.
    if LOCAL.is_symlink():
        parser.error("Refusing to use a symlinked .local directory.")
    if args.command == "reset":
        if not args.confirm:
            parser.error("Reset deletes the local database. Stop the server and pass --confirm.")
        run("manage.py", "check")
        for name in (
            "salty.sqlite3",
            "salty.sqlite3-journal",
            "salty.sqlite3-wal",
            "salty.sqlite3-shm",
        ):
            (LOCAL / name).unlink(missing_ok=True)
        run("manage.py", "migrate", "--noinput")
        print("Local database recreated. Configuration and file storage were preserved.")
        return
    LOCAL.mkdir(exist_ok=True)
    (LOCAL / "files").mkdir(exist_ok=True)
    config_path = LOCAL / "settings.json"
    if not config_path.exists():
        config = json.loads((ROOT / "config.example.json").read_text(encoding="utf-8"))
        config["secret_key"] = secrets.token_urlsafe(64)
        with config_path.open("x", encoding="utf-8") as file:
            json.dump(config, file, indent=2)
        config_path.chmod(0o600)
    run("manage.py", "migrate", "--noinput")
    print("Ready. Start locally: python manage.py runserver 127.0.0.1:8000")


if __name__ == "__main__":
    main()
