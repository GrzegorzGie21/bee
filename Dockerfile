FROM python:3.8

ARG python_env_value=1

ENV PYTHONUNBUFFERED python_env_value
ENV PYTHONDONTWRITEBYTECODE python_env_value

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/