from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    ticket_id: str
    customer_message: str
    history: List[str]
    step: int

class Action(BaseModel):
    classification: str
    priority: str
    response: str
    escalate: bool
    request_info: bool

class Reward(BaseModel):
    score: float