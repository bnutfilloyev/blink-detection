# blink-detection

Blink Detection(Open Close Eye detection)

## Development Requirements

- Python3.8.2
- Pip
- Poetry (Python Package Manager)

### M.L Model Environment

```sh
MODEL_PATH=./ml/model/
MODEL_NAME=model.h5
```
## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── models           - pydantic models for this application.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
    │
    tests                  - pytest
    |
    models                 - Traing data models
    └── datasets           - crop eye datasets
    └── data_collecting.ipynb - data collecting notebook
    └── dataset.csv        - dataset 1D Array
    └── helpers.py         - helper functions
    └── preprocess.py      - preprocessing functions
    └── train.ipynb        - training functions
    └── test.py            - Real Time Camera test function