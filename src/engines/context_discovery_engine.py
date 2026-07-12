from models.incident import Incident
from models.context import Context
from models.investigation_strategy import InvestigationStrategy


class ContextDiscoveryEngine:
    """
    Responsible for reducing uncertainty before reasoning begins.
    """

    def collect_context(
        self,
        incident: Incident,
        classification: str,
        strategy: InvestigationStrategy
    ) -> Context:

        print(f"Incident classified as: {classification}")

        return Context(
            incident_type=classification,
            affected_scope="Unknown",
            observation_layer="Unknown",
            timeline="Unknown",
            recent_changes="Unknown",
            missing_information=[]
        )

  