# DVC Template

This is a repository that can be used as a starting point for projects using DVC.

## Installation

```sh
docker-compose build
```

## Running the pipeline

Open a terminal inside the docker container:
```sh
docker-compose run dev bash
```

Run the pipeline:
```sh
dvc repro
```
