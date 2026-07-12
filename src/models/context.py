from dataclasses import dataclass
from typing import List


@dataclass
class Context:
    """
    Represents all verified information collected
    before reasoning begins.
    """

    incident_type: str

    affected_scope: str

    observation_layer: str

    timeline: str

    recent_changes: str

    missing_information: List[str]