from __future__ import annotations
from datetime import datetime
from sqlalchemy import String, Date, DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from backend.app.models.analysis import Analysis
from backend.app.models.embedding import Embedding

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.app.models.text import Text
    from backend.app.models.project import Project

class Document(Base):
    __tablename__ = "documents"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    language: Mapped[str] = mapped_column(
        String(30),
        default="ko",
    )
    dynasty: Mapped[str | None] = mapped_column(String(80))
    source: Mapped[str | None] = mapped_column(String(255))
    original_date: Mapped[datetime | None] = mapped_column(Date)
    pages: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    project: Mapped["Project"] = relationship(back_populates="documents")
    texts: Mapped[list["Text"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
    )
    analyses: Mapped[list["Analysis"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
    )
    embeddings: Mapped[list["Embedding"]] = relationship(
        back_populates="document",
        cascade="all, delete-orphan",
    )
