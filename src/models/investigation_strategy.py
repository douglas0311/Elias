from dataclasses import dataclass
from typing import List


@dataclass
class InvestigationStrategy:
    """
    Defines how Elias should investigate an incident
    based on technical and business context.
    """

    name: str

    goal: str

    priority: str

    question_limit: int

    strategy_steps: List[str]