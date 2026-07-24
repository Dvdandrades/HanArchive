from __future__ import annotations
from sqlalchemy import Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Location(Base):
    __tablename__ = "locations"

    entity_id: Mapped[int] = mapped_column(
        ForeignKey("entities.id", ondelete="CASCADE"),
        primary_key=True,
    )
    historical_name: Mapped[str | None] = mapped_column(String(250))
    modern_name: Mapped[str | None] = mapped_column(String(250))
    latitude: Mapped[float | None] = mapped_column(Float)
    longitude: Mapped[float | None] = mapped_column(Float)
    country: Mapped[str | None] = mapped_column(String(100))
    region: Mapped[str | None] = mapped_column(String(150))
    entity = relationship(
        "Entity",
        back_populates="location",
    )

    def __repr__(self):
        return f"<Location(name={self.modern_name})>"
