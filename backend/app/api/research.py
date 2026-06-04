from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from fastapi import Depends
from typing import Optional

from app.models.user import User

from app.schemas.research import CreateResearchRequest, ResearchResponse, ResearchListResponse
from app.services.research_services import create_research, get_research_sessions, get_research_by_id, delete_research
from app.services.pdf_services import generate_research_pdf
from app.database.dependencies import get_db

from app.core.dependencies import get_current_user
from app.schemas.common import MessageResponse

from sqlalchemy.orm import Session
from sqlalchemy import select

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

@router.get(
    "",
    response_model=list[ResearchListResponse]
)
def get_research_list(
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_research_sessions(
        db,
        current_user,
        search
    )

@router.get(
    "/{research_id}",
    response_model=ResearchResponse
)
def get_research_detail(
    research_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_research_by_id(db, current_user, research_id)

@router.post(
    "",
    response_model=ResearchResponse
)
def create_research_endpoint(
    request: CreateResearchRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_research(
        db,
        current_user,
        request
    )
    
@router.delete(
    "/{research_id}",
    response_model=MessageResponse
)
def delete_research_endpoint(
    research_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_research(db, current_user, research_id)

@router.get(
    "/{research_id}/pdf"
)
def export_research_pdf(
    research_id: int,
    db: Session = Depends(
        get_db
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    research = get_research_by_id(
        db,
        current_user,
        research_id
    )

    pdf_buffer = (
        generate_research_pdf(
            research
        )
    )

    return StreamingResponse(
        pdf_buffer,
        media_type=
        "application/pdf",
        headers={
            "Content-Disposition":
            f'attachment; filename="research-{research.id}.pdf"'
        }
    )