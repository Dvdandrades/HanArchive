from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="HanArchive API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hanarchive.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "HanArchive API"}