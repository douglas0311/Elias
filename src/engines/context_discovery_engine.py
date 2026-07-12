from models.incident import Incident
from models.context import Context


class ContextDiscoveryEngine:
    """
    Responsible for reducing uncertainty before reasoning begins.
    """

    def collect_context(self, incident: Incident) -> Context:

        incident_type = self.classify_incident(incident)

        print(f"Incident classified as: {incident_type}")

        return Context(
            incident_type=incident_type,
            affected_scope="Unknown",
            observation_layer="Unknown",
            timeline="Unknown",
            recent_changes="Unknown",
            missing_information=[]
        )

    def classify_incident(self, incident: Incident) -> str:
        """
        First attempt to understand what kind of incident we are dealing with.
        """

        return "Unknown"