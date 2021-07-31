FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Additional dependencies
  && apt-get install -y telnet netcat \
  && apt-get install -y libapache2-mod-wsgi-py3 \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/ubuntu/cargamos/

WORKDIR /home/ubuntu/cargamos/

ADD . /home/ubuntu/cargamos/

ENV HOME=/home/ubuntu
ENV APP_HOME=$HOME/cargamos

RUN mkdir $APP_HOME/static && mkdir $APP_HOME/media

WORKDIR $APP_HOME

RUN pip3 install -r /home/ubuntu/cargamos/requirements.txt


COPY ./compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./compose/celery/worker_start /worker_start
RUN sed -i 's/\r$//g' /worker_start
RUN chmod +x /worker_start

COPY ./compose/celery/beat_start /beat_start
RUN sed -i 's/\r$//g' /beat_start
RUN chmod +x /beat_start

COPY ./compose/celery/flower_start /flower_start
RUN sed -i 's/\r$//g' /flower_start
RUN chmod +x /flower_start

ENTRYPOINT ["/entrypoint"]