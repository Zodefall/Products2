# syntax=docker/dockerfile:1
FROM python:3.10.4
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=Drf.settings
WORKDIR /code
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip \
    pip install -r requirements.txt
COPY . /code/