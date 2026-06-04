from datetime import datetime
from pydantic import BaseModel

class CreateResearchRequest(BaseModel):
    topic: str
    
class ResearchResponse(BaseModel):
    id: int
    topic: str
    summary: str
    created_at: datetime
    
    model_config = {
        "from_attributes": True
    }

class ResearchListResponse(BaseModel):
    id: int
    topic: str
    created_at: datetime
    
    model_config = {
        "from_attributes": True
    }
    
class ResearchData(BaseModel):
    overview: str

    key_findings: list[str]

    risks: list[str]

    future_trends: list[str]
    
class ResearchResponse(BaseModel):
    id: int

    topic: str

    research_data: ResearchData

    created_at: datetime

    model_config = {
        "from_attributes": True
    }