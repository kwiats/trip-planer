## Develop app

### environments
- this get environments from backend/.env and override it with .env.local in containers 

backend/.env.local

```bash
POSTGRES_HOST=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=triplane
POSTGRES_DB=postgres-triplane
POSTGRES_PORT=5432

SECRET_KEY=test
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=300
REFRESH_TOKEN_EXPIRE_DAYS=365

CORS_ORIGINS=http://localhost:8083

MINIO_HOST_URL=minio:9000
MINIO_ACCESS_KEY=superuser
MINIO_SECRET_KEY=superuser
MINIO_SECURE=False

FASTAPI_HOST=localhost
FASTAPI_PORT=8000
DEBUG=1
PYTHONBREAKPOINT=pdb.set_trace

CACHE_STORAGE_HOST=redis
CACHE_STORAGE_PORT=6379
CACHE_STORAGE_PASSWORD=redis
CACHE_STORAGE_DB=0
CACHE_STORAGE_EXP=86400

```

### build app

```bash
docker-compose up --build -d
```

### debug with docker pdb++

```bash
docker-compose run --rm --service-ports django
```

or

```bash
./commands/debug.sh
```

### run containers to vscode or pycharm ide then step debug

```bash
docker-compose --profile dev up 
```

### run pytest

```bash
docker-compose --profile test up
docker-compose --profile test run --rm test sh -c "uv run pytest -v --disable-pytest-warnings"
docker-compose --profile test run --rm test sh -c "uv run pytest -v -k <test-name>"
docker-compose --profile test run --rm test sh -c "uv run pytest -v -p no:cov --disable-pytest-warnings"
```
