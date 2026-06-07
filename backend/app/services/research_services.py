from app.models.enums import ResearchStatus
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.research_session import ResearchSession
from app.models.user import User
from app.services.openai_service import generate_research_summary
from app.agents.research_graph import research_graph

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

def get_research_sessions(
    db: Session,
    user: User,
    search: str | None = None,
    page: int = 1,
    page_size: int = 10
):
    statement = (
        select(ResearchSession)
        .where(
            ResearchSession.user_id
            == user.id
        )
    )

    if search:
        statement = statement.where(
            ResearchSession.topic.ilike(
                f"%{search}%"
            )
        )
        
    total = len(db.scalars(statement).all())
    offset = (page - 1) * page_size

    items = db.scalars(
        statement
        .order_by(
            ResearchSession.created_at.desc()
        )
        .offset(offset)
        .limit(page_size)
    ).all()

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size
    }

def create_research(
    db: Session,
    user: User,
    request: CreateResearchRequest
):
    research = ResearchSession(
        user_id=user.id,
        topic=request.topic,
        status=ResearchStatus.PROCESSING.value,
        research_data={}
    )

    db.add(research)
    db.commit()
    db.refresh(research)

    try:
        result = research_graph.invoke(
            {
                "topic": request.topic
            }
        )

        research.research_data = (
            result["final_report"]
        )

        research.status = (
            ResearchStatus.COMPLETED.value
        )

    except Exception:
        research.research_data = {
            {
                "overview": "Failed to generate research.",
                "key_findings": [],
                "risks": [],
                "future_trends": [],
                "sources": []
            }
        }

        research.status = (
            ResearchStatus.FAILED.value
        )

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