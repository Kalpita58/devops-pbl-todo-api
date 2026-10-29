# Todo API - DevOps PBL

A small Python Flask REST API for the DevOps PBL assignment.

## Endpoints

- `GET /` - API welcome information
- `GET /todos` - list tasks
- `POST /todos` - create a task using JSON such as `{"task": "Learn Docker"}`
- `GET /health` - health check

Tasks are stored in memory and reset when the app restarts.

## Run locally on Ubuntu

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

In another terminal, test it:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/todos
curl -X POST http://127.0.0.1:5000/todos \
  -H 'Content-Type: application/json' \
  -d '{"task":"Learn Docker"}'
```

## Run tests

```bash
source .venv/bin/activate
pytest -v
```

## Build and run with Docker

```bash
docker build -t todo-api:latest .
docker run --rm -p 5000:5000 todo-api:latest
```

## Notes

- Jenkinsfile runs pytest and archives a source bundle. Configure Jenkins with a Python 3 installation and access to the repository.
- Ansible and Kubernetes manifests will be added in the next stages.
- Do not commit secrets, tokens, or passwords to Git.
## DevOps Pipeline

This project demonstrates a Flask Todo API deployed through a DevOps pipeline.

### API Endpoints
- GET / : Welcome message
- GET /todos : List all tasks
- POST /todos : Add a new task
- GET /health : Check application health

