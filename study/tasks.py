from celery import Celery

app = Celery('study', backend='redis://localhost:6379/0', broker='redis://localhost:6379')


@app.task(name='study.tasks.add')
def add(x, y):
    return x+y
