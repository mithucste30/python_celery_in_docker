from celery import Celery

app = Celery('tasks', backend='redis://redis', broker='pyamqp://guest@queue//')

@app.task
def add(x, y):
    print(x+y)
    return x + y