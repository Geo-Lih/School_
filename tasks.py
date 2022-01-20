from celery import Celery


app = Celery('tasks', backend='rpc://', broker='amqp://localhost')


app.conf.beat_schedule = {
    '__main__.print_me': {
        'task': '__main__.print_me',
        'args': (1, 3),
        'schedule': 10,
    },
}


@app.task(name='__main__.print_me')
def print_me(a, b):
    print(f'i was printed {a} {b}')

    import time
    time.sleep(5)

    return "My result"

