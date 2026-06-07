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
    status: str
    model_config = {
        "from_attributes": True
    }
    

class CitationItem(BaseModel):
    statement: str
    source_id: int


class SourceItem(BaseModel):
    id: int
    title: str
    url: str


class ResearchData(BaseModel):
    overview: str
    key_findings: list[CitationItem]
    risks: list[CitationItem]
    future_trends: list[CitationItem]
    sources: list[SourceItem]
    
class ResearchResponse(BaseModel):
    id: int
    topic: str
    research_data: ResearchData
    created_at: datetime
    status: str
    model_config = {
        "from_attributes": True
    }
    
    
class PaginatedResearchResponse(
    BaseModel
):
    items: list[ResearchListResponse]
    total: int
    page: int
    page_size: int
