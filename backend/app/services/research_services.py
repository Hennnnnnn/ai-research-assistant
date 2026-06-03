from sqlalchemy.orm import Session

from app.models.research_session import ResearchSession
from app.models.user import User

from app.schemas.research import CreateResearchRequest

def create_research(db: Session, user: User, request: CreateResearchRequest):
    research = ResearchSession(
        user_id=user.id,
        topic=request.topic,
        summary=f"Research result for {request.topic}"
    )
    
    db.add(research)
    db.commit()
    db.refresh(research)
    
    return research