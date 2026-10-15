# SE_Docker

[![Python CI](https://github.com/danialtavakoli/SE_Docker/actions/workflows/ci.yml/badge.svg)](https://github.com/danialtavakoli/SE_Docker/actions/workflows/ci.yml)
![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED)

A small Python project that demonstrates a complete **CI/CD workflow**: automated testing with `pytest`, containerisation with **Docker**, and a **GitHub Actions** pipeline that builds, tests and publishes the image to Docker Hub. Built for a Software Engineering course.

## Pipeline

On every push or pull request to `main`, `.github/workflows/ci.yml`:

1. **test**: sets up Python 3.11, installs dependencies and runs `pytest`
2. **docker**: builds the image and runs the test suite inside the container
3. On pushes only, logs in to Docker Hub and pushes `danialtk/se_docker` (needs `DOCKER_USERNAME` and `DOCKER_PASSWORD` repository secrets)

## Project structure

```
main.py                        # arithmetic functions: add, subtract, multiply, divide
test_main.py                   # pytest unit tests, including the divide-by-zero case
Dockerfile                     # python:3.11-slim image that runs the tests
requirements.txt               # test dependency (pytest)
.github/workflows/ci.yml       # CI/CD pipeline
```

## Run locally

```bash
pip install -r requirements.txt
pytest -v
python main.py
```

## Run with Docker

```bash
docker build -t se_docker .
docker run --rm se_docker
```

The container runs the test suite and exits with a non-zero status if any test fails.
