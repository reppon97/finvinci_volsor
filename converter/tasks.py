from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


# Our scheduled task for celery-beat
@shared_task
def scheduled_job():
    from converter.utils.db_updater import save_to_db

    save_to_db()
    logger.info("Scheduled job succeed")
