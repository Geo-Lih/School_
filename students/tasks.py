from datetime import datetime, timedelta

from celery import shared_task

from .models import Logger


@shared_task
def delete_log():
    s_date = (datetime.today().date() - timedelta(days=7))
    result = Logger.objects.filter(created=s_date)

    for i in result:
        Logger.objects.filter(pk=i.pk).delete()

    return f"Last date: {s_date}. Deleted {result.count()} rows."


@shared_task
def send_email(**kwargs):
    name = kwargs['name']
    email = kwargs['email']
    message = kwargs['message']

    return f"Message was sent to {name} on {email} , {datetime.now()} with next text: {message} "
