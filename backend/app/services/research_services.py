from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.research_session import ResearchSession
from app.models.user import User
from app.services.openai_service import generate_research_summary

from app.schemas.research import CreateResearchRequest

from fastapi import HTTPException

def get_research_by_id(
    db: Session,
    user: User,
    research_id: int
):
    statement = select(
        ResearchSession
    ).where(
        ResearchSession.id == research_id,
        ResearchSession.user_id == user.id
    )
    
    research = db.scalar(statement)
    
    if research is None:
        raise HTTPException(
            status_code=404,
            detail="Research not found"
        )
        
    return research

def get_research_sessions(db: Session, user: User):
    statement = (
        select(ResearchSession)
        .where(ResearchSession.user_id == user.id)
        .order_by(ResearchSession.created_at.desc())
    )
    
    return db.scalars(statement).all()

def create_research(db: Session, user: User, request: CreateResearchRequest):
    try:
        research_data = (
            generate_research_summary(
                request.topic
            )
        )

    except Exception:
        research_data = {
            "overview":
                "Failed to generate research.",

            "key_findings": [],

            "risks": [],

            "future_trends": []
        }

    research = ResearchSession(
        user_id=user.id,
        topic=request.topic,
        research_data=research_data
    )

    db.add(research)
    db.commit()
    db.refresh(research)

    return research

def delete_research(db: Session, user: User, research_id: int):
    statement = select(
        ResearchSession
    ).where(
        ResearchSession.id == research_id,
        ResearchSession.user_id == user.id
    )
    
    research = db.scalar(statement)
    
    if research is None:
        raise HTTPException(
            status_code=404,
            detail="Research not found"
        )
        
    db.delete(research)
    db.commit()
    
    return {
        "message": "Research deleted"
    }