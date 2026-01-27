from celery import Celery

"""
Celery app configuration.

Why separate file?
- Centralized config
- Used by both API and worker
"""

celery_app = Celery(
    "ai_support_backend",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["app.tasks.ai_tasks"]
)

# 🔥 THIS LINE FIXES YOUR ERROR
celery_app.autodiscover_tasks(["app.tasks"])

# Optional but recommended
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
