## Tasky API

## Installation

- Create the Virtual Environment

```
$ python --version     #3.12.5
$ python -m venv venv
```

- Activate the Virtual Environment

On Windows:

```
$ .\venv\Scripts\Activate.ps1
```

- Install dependencies

```
$ pip --version       #24.2
$ pip install -r requirements.txt
```

## Run the API locally
- Run Migrations

Note: Set `DATABASE_URL` variable in `.env` file

```
$ alembic upgrade head
```

- Run the API in debug mode

```
$ uvicorn app.main:app --reload
```

## Run the API in Docker

- Build and Run the containers

```
$ docker compose build
$ docker compose up -d
```

- Run Migrations

Note: Set `DATABASE_URL` variable in `.env` file

```
$ alembic upgrade head
```

- Stop the containers

```
$ docker compose stop
```