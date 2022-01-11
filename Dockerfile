FROM python:3.8

ENV PYTHOBUFFERED 1
ENV PYTHOWRUTEBYTECODE 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/