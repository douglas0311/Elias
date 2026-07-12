from dataclasses import dataclass


@dataclass
class Question:
    """
    Represents a question used to reduce uncertainty.
    """

    text: str

    purpose: str

    priority: int