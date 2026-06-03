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