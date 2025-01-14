# Stage 1
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS base

# Sync the project into a new environment
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gcc \
    libpq-dev \
    libpq5 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Add uv to the path
ENV PATH="/root/.local/bin/:$PATH"

# Stage 2
FROM base AS dependencies

# Install the project's dependencies using the lockfile and settings
COPY pyproject.toml uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project # --no-dev


# Stage 3
FROM python:3.12-slim AS final

# Copy the built project
COPY --from=dependencies /app /app

# Copy the project into the image
COPY ./src /app/src

WORKDIR /app/src
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"



COPY ./docker/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./docker/django/run.sh /run.sh
RUN sed -i 's/\r$//g' /run.sh && chmod +x /run.sh

COPY ./docker/django/check_superuser.sh /check_superuser.sh
RUN sed -i 's/\r$//g' /check_superuser.sh && chmod +x /check_superuser.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash", "-c", "/check_superuser.sh && /run.sh"]