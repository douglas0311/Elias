from models.investigation_strategy import InvestigationStrategy


class StrategyEngine:

    def choose_strategy(self, classification: str) -> InvestigationStrategy:

        return InvestigationStrategy(
            name="Learning",
            goal="Understand the incident.",
            priority="Learning",
            question_limit=20,
            strategy_steps=[]
        )