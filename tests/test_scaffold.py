import json
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.core.exceptions import ImproperlyConfigured
from django.db import OperationalError
from django.test import SimpleTestCase, TestCase

from salty.config import load_config


class ConfigTests(SimpleTestCase):
    def test_missing_config_has_actionable_error(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesMessage(ImproperlyConfigured, "scripts/dev.py setup"):
                load_config(Path(directory) / "missing.json")

    def test_bad_config_never_echoes_values(self):
        for data in (
            {"environment": "production"},
            {"environment": "development", "secret_key": "PRIVATE"},
            [],
        ):
            with self.subTest(data=data), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "settings.json"
                path.write_text(json.dumps(data))
                with self.assertRaises(ImproperlyConfigured) as error:
                    load_config(path)
                self.assertNotIn("PRIVATE", str(error.exception))

    def test_malformed_config_is_redacted(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "settings.json"
            path.write_text("PRIVATE invalid json")
            with self.assertRaisesMessage(ImproperlyConfigured, "missing or invalid"):
                load_config(path)


class HealthTests(TestCase):
    def test_health_uses_migrated_database(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})
        self.assertIn("no-store", response["Cache-Control"])

    def test_database_failure_is_redacted(self):
        with patch("salty.views.connection.cursor", side_effect=OperationalError("PRIVATE")):
            response = self.client.get("/health/")
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.json(), {"status": "unavailable"})

    def test_unmigrated_database_is_not_ready(self):
        with patch("salty.views.connection.cursor") as cursor:
            cursor.return_value.__enter__.return_value.fetchone.return_value = (0,)
            self.assertEqual(self.client.get("/health/").status_code, 503)

    def test_no_write_method_or_file_routes(self):
        self.assertEqual(self.client.post("/health/").status_code, 405)
        self.assertEqual(self.client.get("/.local/settings.json").status_code, 404)
        self.assertEqual(self.client.get("/files/example.txt").status_code, 404)

    def test_home_describes_actual_state(self):
        self.assertContains(self.client.get("/"), "No school accounts")
