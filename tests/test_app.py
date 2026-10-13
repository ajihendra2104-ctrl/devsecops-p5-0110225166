
import tempfile
import unittest
from pathlib import Path

from src.validator import validate_title
from src.note import Note
from src.manager import NoteManager


class SecureNotesTests(unittest.TestCase):
    def test_title_is_trimmed(self):
        self.assertEqual(validate_title("  Kuliah  "), "Kuliah")

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("  ")

    def test_long_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("A" * 101)

    def test_note_display(self):
        note = Note("Tugas", "Belajar Python")
        self.assertEqual(
            note.display(), "Tugas\nBelajar Python"
        )

    def test_note_is_saved_and_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "notes.json"
            manager = NoteManager(path)
            manager.add_note("Tugas", "Belajar CI/CD")

            self.assertEqual(
                manager.get_notes()[0]["content"],
                "Belajar CI/CD"
            )


if __name__ == "__main__":
    unittest.main()
