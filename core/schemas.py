from pydantic import BaseModel, Field
from typing import Optional

class EmailRequest(BaseModel):
    sender: str = Field(..., example = 'client@vendor.com')
    subject: str = Field(..., example = "Urgent Contact Update")
    body: str = Field(..., example = "Please sign the attached addendum by EOD.")
class EmailTriageResponse(BaseModel):
    category: str = Field(..., description="Actions Required | Informational | Newsletter | Low Priority")
    summary : str
    action_item: str
    quick_reply: str
    latency_seconds: float