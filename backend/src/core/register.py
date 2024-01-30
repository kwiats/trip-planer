from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.attraction.routes.router import router as attraction_router
from src.auth.routes import auth_router
from src.core.configs import CORS_ORIGINS
from src.core.database import Base, engine
from src.core.logger import LoggerSetup
from src.middleware.log_middleware import LoggingMiddleware
from src.users.routes import router as users_router
from src.file.router import file_router


def _init_app(version: str) -> FastAPI:
    Base.metadata.create_all(bind=engine)
    return FastAPI(version=version, debug=True)


def _read_version() -> str:
    try:
        with open("src/VERSION.txt", "r") as version_file:
            version = version_file.read()
            return version.strip()
    except FileNotFoundError:
        with open("src/VERSION.txt", "w") as version_file:
            version_file.write("0.0.0")
        return "0.0.0"


def register_app():
    VERSION = _read_version()
    # config = config.Settings() if we create Settings object we can put this to init_app
    app = _init_app(version=VERSION)

    register_router(app)
    # we can initialize all configurations, middlewares, cors etc. here
    register_logger()
    register_middleware(app)
    return app


def register_middleware(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def register_router(app: FastAPI):
    app.include_router(attraction_router, prefix="/attractions")
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(users_router, prefix="/me")
    app.include_router(file_router, prefix="/files", tags=["files"])


def register_logger() -> LoggerSetup:
    return LoggerSetup()
