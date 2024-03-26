from celery import shared_task

@shared_task
def add(x, y):
    print(f"Adding {x} + {y}")
    return x + y

@shared_task
def multiply(x, y):
    print(f"Multiplying {x} * {y}")
    return x * y