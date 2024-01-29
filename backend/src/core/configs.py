import os

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_DB_NAME = os.getenv("POSTGRES_DB", "postgres")
SECRET_KEY = os.getenv("SECRET_KEY", "asd123")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "300"))

MINIO_HOST_URL = os.getenv("MINIO_HOST_URL")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_SECURE = os.getenv("MINIO_SECURE", False) == "True"

CORS_ORIGINS_ENV = os.getenv("CORS_ORIGINS", "http://localhost:8081")
CORS_ORIGINS = CORS_ORIGINS_ENV.split(',')