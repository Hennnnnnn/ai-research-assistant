from app.tasks.research_tasks import *

celery_app.autodiscover_tasks(
    ["app.tasks"]
)