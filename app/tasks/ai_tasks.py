from app.core.celery_app import celery_app
from app.services.ai_service import analyze_message
from app.core.logger import get_logger

logger = get_logger(__name__)

"""
Celery task wrapper.

Why wrapper?
- Keeps ai_service clean
- Celery should not touch HTTP or DB routing
"""

@celery_app.task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=5,
    retry_kwargs={"max_retries": 3}
)


def process_message_ai(self, message_id: str, content: str, ticket_id: str):

    logger.info(
        f"AI task started | message_id={message_id} ticket_id={ticket_id}"
    )
    """
    Background AI processing task.

    - Retries on failure
    - Runs outside FastAPI process
    """
    analyze_message(
        message_id=message_id,
        content=content,
        ticket_id=ticket_id
    )

    logger.info(
        f"AI task completed | message_id={message_id}"
    )