FROM python:3.11.4-alpine3.18
WORKDIR /code

RUN python -m pip install poetry
COPY . .
RUN poetry install
RUN poetry run python manage.py migrate
CMD poetry run python manage.py runserver
