
import json
from pathlib import Path
from src.note import Note


class NoteManager:
    def __init__(self, storage_path="notes.json"):
        self.storage_path = Path(storage_path)

    def add_note(self, title: str, content: str) -> Note:
        note = Note(title, content)
        notes = self.get_notes()
        notes.append({
            "title": note.title,
            "content": note.content
        })

        self.storage_path.write_text(
            json.dumps(notes, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        return note

    def get_notes(self) -> list:
        if not self.storage_path.exists():
            return []

        data = json.loads(
            self.storage_path.read_text(encoding="utf-8")
        )

        if not isinstance(data, list):
            raise ValueError("Invalid notes storage format.")

        return data
