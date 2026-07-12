from models.context import Context
from models.investigation_strategy import InvestigationStrategy


class StrategyEngine:
    """
    Chooses the investigation strategy based on
    technical and business context.
    """

    def choose_strategy(self, context: Context) -> InvestigationStrategy:
        pass