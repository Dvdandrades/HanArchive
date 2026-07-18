from __future__ import annotations
from datetime import date
from sqlalchemy import Date, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Event(Base):
    __tablename__ = "events"

    entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id", ondelete="CASCADE"),
        primary_key=True,
    )
    title: Mapped[str | None] = mapped_column(String(300))
    start_date: Mapped[date | None] = mapped_column(Date)
    end_date : Mapped[date | None] = mapped_column(Date)
    dynasty: Mapped[str | None] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(Text)
    entity = relationship(
        "Entity",
        back_populates="event",
    )

    def __repr__(self):
        return f"<Event(title={self.title})>"