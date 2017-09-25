FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat python-m2crypto appt

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN pip install -U pip
RUN pip install -Ur requirements.txt

RUN python /code/manage.py collectstatic --noinput
RUN python manage.py makemigrations apks
RUN python manage.py migrate