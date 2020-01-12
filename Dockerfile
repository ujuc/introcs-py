FROM python:3.7-slim

RUN apt update \
    && apt install -y -qq python3-pygame \
    && python -m pip install poetry

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install
