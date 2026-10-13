
from dataclasses import dataclass
from src.validator import validate_title


@dataclass
class Note:
    title: str
    content: str

    def __post_init__(self):
        self.title = validate_title(self.title)

        if not isinstance(self.content, str):
            raise ValueError("Content must be text.")

    def display(self) -> str:
        return f"{self.title}\n{self.content}"
