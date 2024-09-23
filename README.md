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

- Run the API in debug mode

```
$ uvicorn app.main:app --reload
```