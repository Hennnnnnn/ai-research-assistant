from celery import Celery
from app.core.config import (
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND
)

celery_app = Celery(
    "research_worker",
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
    include=[
        "app.tasks.research_tasks"
    ]
)
celery_app.conf.update(
    task_track_started=True
)