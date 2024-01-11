# RATS-web
RATS - Reborned CATS web part
## Deployment !!!OUTDATED!!!
### Manual with poetry
1. Set up and run postgresql
2. Switch to the `web`
3. Create `.env` file and fill it with variables from `.devenv`
4. `pip install poetry`
5. `poetry install`
6. `poetry run python -m app.database.session`
7. `poetry run uvicorn app.main:app --reload`
### Docker compose
1. Create `.env` file and fill it with variables from `.devenv`
2. `docker-compose up`
## Project structure
```
app/
├── main.py                 # main router
├── settings.py             # pydantic settings
├── api/
│   └── ...
├── schemas/                # pydantic schemas
│   └── ...
├── service/                # business logic
│   └── ...
└── database/
    ├── models.py
    └── session.py          # Database connection +
                            # + models init on file run
```
