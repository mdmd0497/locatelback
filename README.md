# Fastapi base template for Python API projects

Base template project to expand your ideas without need to set up the project from scratch.

## Installation

### Pip

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Poetry

Install poetry 
```
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
$ poetry install
```

## Usage

### Pip

```bash
$ uvicorn config:app --host=0.0.0.0 --port=5003 --reload --log-level=info
```

### Poetry

```bash
$ poetry run start
```

### Docker
    
```bash
$ docker build -t fastapi-base .
$ docker run -p 5003:5003 -d fastapi-base
```
### Build database in Mongo
```bash
$ docker run -d -p 27017:27017 --name=prueba mongo:4.2

```


