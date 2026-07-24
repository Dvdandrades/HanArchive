from __future__ import annotations
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Person(Base):
    __tablename__ = "persons"

    entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id", ondelete="CASCADE"),
        primary_key=True,
    )
    canonical_name: Mapped[str | None] = mapped_column(String(250))
    courtesy_name: Mapped[str | None] = mapped_column(String(250))
    pen_name: Mapped[str | None] = mapped_column(String(250))
    birth_year: Mapped[int | None] = mapped_column(Integer)
    death_year: Mapped[int | None] = mapped_column(Integer)
    dynasty: Mapped[str | None] = mapped_column(String(100))
    occupation: Mapped[str | None] = mapped_column(String(200))
    entity = relationship(
        "Entity",
        back_populates="person",
    )

    def __repr__(self):
        return f"<Person(name={self.canonical_name})>"
