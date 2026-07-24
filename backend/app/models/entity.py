from __future__ import annotations
from datetime import datetime
from enum import Enum
from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class EntityType(str, Enum):
    PERSON = "person"
    LOCATION = "location"
    EVENT = "event"
    ORGANIZATION = "organization"
    DYNASTY = "dynasty"
    TITLE = "title"
    OTHER = "other"


class Entity(Base):
    __tablename__ = "entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    text_id: Mapped[int] = mapped_column(
        ForeignKey("texts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    entity_type: Mapped[EntityType] = mapped_column(
        SQLEnum(EntityType),
        nullable=False,
        index=True,
    )
    surface: Mapped[str] = mapped_column(
        String(300),
        nullable=False,
    )
    normalized: Mapped[str | None] = mapped_column(String(300))
    confidence: Mapped[float] = mapped_column(
        Float,
        default=1.0,
    )
    start_offset: Mapped[int] = mapped_column(Integer)
    end_offset: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    text = relationship(
        "Text",
        back_populates="entities",
    )
    person = relationship(
        "Person",
        back_populates="entity",
        uselist=False,
        cascade="all, delete-orphan",
    )
    location = relationship(
        "Location",
        back_populates="entity",
        uselist=False,
        cascade="all, delete-orphan",
    )
    event = relationship(
        "Event",
        back_populates="entity",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return (
            f"<Entity(id={self.id}, type={self.entity_type}, surface='{self.surface}')>"
        )
