from celery import shared_task


@shared_task
def debug_cron_task():
    print("Cron is running")
