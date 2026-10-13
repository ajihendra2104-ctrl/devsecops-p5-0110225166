
import argparse
from src.manager import NoteManager


def main():
    parser = argparse.ArgumentParser(
        description="SecureNotes: a simple note manager"
    )
    parser.add_argument("--title", help="Note title")
    parser.add_argument("--content", help="Note content")
    parser.add_argument(
        "--list",
        action="store_true",
        help="List saved notes"
    )
    args = parser.parse_args()

    manager = NoteManager()

    if args.list:
        for note in manager.get_notes():
            print(f"{note['title']}: {note['content']}")
    elif args.title is not None and args.content is not None:
        note = manager.add_note(args.title, args.content)
        print(f"Saved note: {note.title}")
    else:
        parser.error("Provide --list or both --title and --content.")


if __name__ == "__main__":
    main()
