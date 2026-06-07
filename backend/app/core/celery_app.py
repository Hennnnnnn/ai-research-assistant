from celery import Celery

celery_app = Celery(
    "research_worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=[
        "app.tasks.research_tasks"
    ]
)
celery_app.conf.update(
    task_track_started=True
)