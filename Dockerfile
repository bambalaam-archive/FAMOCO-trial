FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat python-m2crypto aapt

RUN pip install -U pip
RUN pip install -Ur requirements.txt

RUN python manage.py makemigrations apks

CMD [ "python", "manage.py runserver" ]