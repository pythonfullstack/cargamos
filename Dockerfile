FROM python:3.7

RUN mkdir -p /home/ubuntu/cargamos/
RUN apt-get install libapache2-mod-wsgi-py3

WORKDIR /home/ubuntu/cargamos/

ADD . /home/ubuntu/cargamos/

ENV HOME=/home/ubuntu
ENV APP_HOME=$HOME/cargamos

RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media

WORKDIR $APP_HOME

RUN pip3 install -r /home/ubuntu/cargamos/requirements.txt