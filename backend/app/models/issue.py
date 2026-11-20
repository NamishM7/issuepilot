
from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy import String, Text, JSON, DateTime, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Issue(Base):
    
    __tablename__ = "issues"

    # Primary key
    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    # Issue title
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    # Issue description
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # GitHub repository
    repository: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # Issue labels
    labels: Mapped[list[str]] = mapped_column(
        JSON,
        default=list,
        nullable=False
    )

    # Issue status
    state: Mapped[str] = mapped_column(
        String(20),
        default="open",
        nullable=False
    )

    # Creation timestamp
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
