from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey, Text, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from backend.app.models.entity import Entity
from backend.app.models.token import Token
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from backend.app.models.document import Document


class Text(Base):
    __tablename__ = "texts"
    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    version: Mapped[str] = mapped_column(
        String(50),
        default="original",
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    normalized_content: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    document: Mapped["Document"] = relationship(back_populates="texts")
    tokens: Mapped[list["Token"]] = relationship(
        back_populates="text",
        cascade="all, delete-orphan",
    )
    entities: Mapped[list["Entity"]] = relationship(
        back_populates="text",
        cascade="all, delete-orphan",
    )
