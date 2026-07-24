from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.routes_documents import router as documents_router
from app.api.routes_analysis import router as analysis_router
from app.api.routes_search import router as search_router
from app.api.routes_statistics import router as statistics_router
from app.api.routes_auth import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application started")
    yield
    print("Application stopped")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(documents_router, prefix="/api/documents", tags=["Documents"])
app.include_router(analysis_router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(search_router, prefix="/api/search", tags=["Search"])
app.include_router(statistics_router, prefix="/api/statistics", tags=["Statistics"])


@app.get("/")
async def root():
    return {"project": settings.PROJECT_NAME, "version": settings.VERSION}


@app.get("/health")
async def health():
    return {"status": "healthy"}
