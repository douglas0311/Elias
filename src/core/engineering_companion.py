from models.incident import Incident
from engines.context_discovery_engine import ContextDiscoveryEngine
from engines.classification_engine import ClassificationEngine
from engines.strategy_engine import StrategyEngine

class EngineeringCompanion:
    """
    Main orchestrator of Elias.
    Coordinates the reasoning process.
    """

    def __init__(self):
        self.context_engine = ContextDiscoveryEngine()
        self.classification_engine = ClassificationEngine()
        self.strategy_engine = StrategyEngine()

    def investigate(self, incident: Incident):

        classification = self.classification_engine.classify(incident)

        strategy = self.strategy_engine.choose_strategy(classification)

        context = self.context_engine.collect_context(
            incident,
            classification,
            strategy
    )

        return context