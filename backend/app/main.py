from fastapi import FastAPI

app = FastAPI(title="HanArchive API")

@app.get("/")
def root():
    return {"message": "HanArchive API"}

@app.post("/documents")
def post_documents():
    pass

@app.get("/documents")
def get_all_documents():
    pass

@app.get("/documents/{id}")
def get_one_documents():
    pass