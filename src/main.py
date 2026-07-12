from datetime import datetime

from models.incident import Incident
from core.engineering_companion import EngineeringCompanion


incident = Incident(
    title="502 after deployment",
    description="All users receive a 502 error after today's deployment.",
    created_at=datetime.now()
)

elias = EngineeringCompanion()

context = elias.investigate(incident)

print(context)