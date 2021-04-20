FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update && apt-get update -y && pip install --no-cache-dir -r requirements.txt
COPY . /code/