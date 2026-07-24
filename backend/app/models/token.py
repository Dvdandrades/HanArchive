from __future__ import annotations
from sqlalchemy import String, Integer, Float, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from backend.app.models.text import Text


class Token(Base):
    __tablename__ = "tokens"
    __table_args__ = (
        Index("ix_token_surface", "surface"),
        Index("ix_token_lemma", "lemma"),
        Index("ix_token_pos", "pos"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    text_id: Mapped[int] = mapped_column(
        ForeignKey("texts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    token_index: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    surface: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )
    lemma: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
    )
    pos: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    reading: Mapped[str | None] = mapped_column(String(120))
    script: Mapped[str | None] = mapped_column(String(30))
    start_char: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    end_char: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
    confidence: Mapped[float | None] = mapped_column(Float)
    text: Mapped["Text"] = relationship(back_populates="tokens")
