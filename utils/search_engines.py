from dataclasses import dataclass
from tkinter import IntVar


@dataclass
class SearchEngine:
    """Dataclass for storing search engine information."""

    name: str
    search_str: str
    category: str

    def __post_init__(self):
        self.variable = IntVar()