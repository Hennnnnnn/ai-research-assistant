from fastapi import APIRouter
from fastapi import Depends

from app.models.user import User

from app.schemas.research import (
    CreateResearchRequest,
    ResearchResponse
)

from app.services.research_services import (
    create_research
)

from app.database.dependencies import (
    get_db
)

from app.core.dependencies import (
    get_current_user
)

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/research",
    tags=["Research"]
)

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