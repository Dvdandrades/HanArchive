from fastapi import FastAPI

app = FastAPI(title="HanArchive API")

@app.get("/")
def root():
    return {"message": "HanArchive API"}