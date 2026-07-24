from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentUpdate


def create_document(db: Session, document: DocumentCreate) -> Document:
    db_document = Document(
        title=document.title,
        language=document.language,
        dynasty=document.dynasty,
        project_id=document.project_id,
        description=document.description,
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document


def get_document(db: Session, document_id: int) -> Document | None:
    return db.get(Document, document_id)


def get_documents(db: Session, skip: int = 0, limit: int = 100) -> Sequence[Document]:
    stmt = (
        select(Document).offset(skip).limit(limit).order_by(Document.created_at.desc())
    )

    return db.scalars(stmt).all()


def get_documents_by_project(db: Session, project_id: int) -> Sequence[Document]:
    stmt = (
        select(Document)
        .where(Document.project_id == project_id)
        .order_by(Document.created_at.desc())
    )

    return db.scalars(stmt).all()


def update_document(
    db: Session, db_document: Document, document: DocumentUpdate
) -> Document:
    values = document.model_dump(exclude_unset=True)

    for key, value in values.items():
        setattr(db_document, key, value)

    db.commit()
    db.refresh(db_document)
    return db_document


def delete_document(db: Session, db_document: Document) -> None:
    db.delete(db_document)
    db.commit()


def search_documents(db: Session, query: str) -> Sequence[Document]:
    stmt = (
        select(Document)
        .where(Document.title.ilike(f"%{query}%"))
        .order_by(Document.created_at.desc())
    )

    return db.scalars(stmt).all()
