from models.incident import Incident


class ClassificationEngine:
    """
    Determines the operational context of an incident
    before the investigation begins.
    """

    def classify(self, incident: Incident):
        return "Unknown"