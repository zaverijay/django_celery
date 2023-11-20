from celery import shared_task
from time import sleep

@shared_task
def sub(a, b):
    sleep(10)
    return a-b