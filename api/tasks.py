from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def process_message(self, email, message):
    time.sleep(10)  # Simulate long task
    logger.info(f"Processed message for {email}: {message}")
    return f"Done processing {email}"
