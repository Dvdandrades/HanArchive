from celery import Celery
from app.core.config import settings

celery = Celery(
    "HanArchive",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery.conf.update(
    task_serialize="json",
    result_serialize="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    result_expires=3600,
)