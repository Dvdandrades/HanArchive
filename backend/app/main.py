from fastapi import FastAPI, Depends, HTTPException
from db.session import get_db
from models.models import Document
from sqlalchemy.orm import Session
from schemas.schemas import DocumentCreate, DocumentResponse

app = FastAPI(title="HanArchive API")

@app.get("/")
def root():
    return {"message": "HanArchive API"}

@app.post("/documents")
def create_document(document_in: DocumentCreate, db: Session = Depends(get_db)):
    new_document = Document(
        title=document_in.title,
        language=document_in.language,
        original_text=document_in.original_text
    )
    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return {"id": new_document.id}

@app.get("/documents", response_model=DocumentResponse)
def get_all_documents(db: Session = Depends(get_db)):
    documents = db.query(Document).all()
    return documents
    

@app.get("/documents/{document_id}", response_model=DocumentResponse)
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document.id).first()

    if document is None:
        raise HTTPException(status_code=404, detai="Document not found")
    
    return document