from dataclasses import dataclass
from datetime import datetime


@dataclass
class Incident:
    """
    Represents the starting point of an engineering investigation.
    """

    title: str
    description: str
    created_at: datetime