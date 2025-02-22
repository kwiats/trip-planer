FROM python:3.12-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gdal-bin \
    libgdal-dev \
    binutils \
    libproj-dev \
    libgeos++-dev \
    proj-bin \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin/:$PATH"

FROM builder AS final

COPY --from=builder /app /app

COPY pyproject.toml uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --group test

COPY ./src /app/src

ENV PYTHONPATH=/app/src

WORKDIR /app

ENTRYPOINT ["sh", "-c", "uv run pytest /app/src/tests"]
