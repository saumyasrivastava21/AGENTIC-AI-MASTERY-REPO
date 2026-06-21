from typing import Literal
from pydantic import BaseModel, Field


class RouteDecision(BaseModel):
    route: Literal["math", "research", "coding", "summary", "general"] = Field(
        description="The best route for the user query."
    )
    tool_input: str = Field(
        description="Clean input that should be passed to the selected tool."
    )
    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence score between 0 and 1."
    )
    reason: str = Field(
        description="Short reason for choosing this route."
    )


class AgentResponse(BaseModel):
    query: str
    route: str
    tool_input: str
    tool_output: str
    final_answer: str
    confidence: float
    reason: str