def validate_title(title: str) -> str:
    """Validate and normalize a note title."""
    if not isinstance(title, str):
        raise ValueError("Title must be text.")

    title = title.strip()

    if not title:
        raise ValueError("Title cannot be empty.")

    if len(title) > 100:
        raise ValueError("Title must not exceed 100 characters.")

    return title
