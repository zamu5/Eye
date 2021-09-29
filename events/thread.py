from eye.settings import task_queue
from .models import Event
from django.utils.timezone import make_aware


def start_queue():
    while True:
        event = task_queue.get()
        print(f'creating new register of event {event["session_id"]}')
        Event.objects.create(**event).save()
        task_queue.task_done()