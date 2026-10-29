from pydantic import BaseModel, Field

class ResearchRequest(BaseModel):
    topic: str = Field(..., min_length=3, max_length=500)

class ResearchResponse(BaseModel):
    topic: str
    research_plan: str
    research_analysis: str
    research_review: str
