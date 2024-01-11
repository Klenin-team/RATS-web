FROM python:3.11.4-alpine3.18

WORKDIR /code

RUN python -m pip install poetry
COPY . .
RUN poetry install
CMD poetry run python -m app.utils.create_database
