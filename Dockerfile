FROM python:3.9.15-slim-buster AS builder

ENV TZ=UTC

RUN pip install --upgrade pip

WORKDIR /engineering

COPY ./poetry.lock  /engineering/poetry.lock
COPY ./pyproject.toml /engineering/pyproject.toml

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip uninstall poetry -y
RUN pip install -r requirements.txt --no-cache-dir

FROM builder AS project

COPY ./engineering /engineering/engineering/

RUN mkdir "images"

ENTRYPOINT ["python", "engineering/run.py"]
