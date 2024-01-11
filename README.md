# RATS-web
RATS - Reborned CATS web part
## Deployment !!!OUTDATED!!!
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
2. `docker-compose up`
## Project structure
```
app/
├── main.py                 # main router
├── settings.py             # pydantic settings
├── api/
│   └── routers.py
├── schemas/                # pydantic schemas
│   ├── user.py
│   ├── problem.py
│   ├── contest.py
│   └── ...
├── service/                # business logic
│   ├── authorization/
│   │   └── service.py
│   ├── solution_pulling/
│   │   └── service.py
│   └── ...
└── database/
    ├── models.py
    └── session.py
```
