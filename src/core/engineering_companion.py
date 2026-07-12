from models.incident import Incident
from engines.context_discovery_engine import ContextDiscoveryEngine


class EngineeringCompanion:
    """
    Main orchestrator of Elias.
    Coordinates the reasoning process.
    """

    def __init__(self):
        self.context_engine = ContextDiscoveryEngine()

    def investigate(self, incident: Incident):
        return self.context_engine.collect_context(incident)