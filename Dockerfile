FROM python:3.6.2

RUN pip install celery

WORKDIR /usr/src/app

ENTRYPOINT ["/bin/bash"]