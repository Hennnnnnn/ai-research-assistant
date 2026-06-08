from datetime import datetime

from app.models.enums import ResearchStatus
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.database.base import Base


class ResearchSession(Base):
    __tablename__ = "research_sessions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    topic: Mapped[str] = mapped_column(
        String(255)
    )

    research_data: Mapped[dict] = mapped_column(
        JSON,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User"
    )
    
    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default=ResearchStatus.PENDING.value
    )
    
    progress_message: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        default="Queued"
    )