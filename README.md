# RATS-web
RATS - Reborned CATS web part
## Deployment
### Manual with poetry
1. Set up and run postgresql
2. Switch to the `web`
3. Create `.env` file and fill it with variables from `.devenv`
4. `pip install poetry`
5. `poetry install`
6. `poetry run python manage.py migrate`
7. `poetry run python manage.py runserver`
### Docker compose
1. Create `.env` file and fill it with variables from `.devenv`
2. docker-compose up
