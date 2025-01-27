# Stage 1
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

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
    gdal-bin \
    libgdal-dev \
    binutils \
    libproj-dev \
    libgeos++-dev \
    proj-bin \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin/:$PATH"

# Stage 2
FROM builder AS dependencies

# Install the project's dependencies using the lockfile and settings
COPY pyproject.toml uv.lock /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# Stage 3
FROM python:3.12-slim AS final

# Install GDAL and other required system libraries in the final stage
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libpq5 \
    gdal-bin \
    libgdal32 \
    && rm -rf /var/lib/apt/lists/*

# Copy the built project
COPY --from=dependencies /app /app

# Copy the project into the image
COPY ./src /app/src

WORKDIR /app/src
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH" \
    # Set GDAL environment variables
    GDAL_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgdal.so \
    GEOS_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/libgeos_c.so

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./docker/django/run.sh /run.sh
RUN sed -i 's/\r$//g' /run.sh && chmod +x /run.sh

COPY ./docker/django/check_superuser.sh /check_superuser.sh
RUN sed -i 's/\r$//g' /check_superuser.sh && chmod +x /check_superuser.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/bin/bash", "-c", "/check_superuser.sh && /run.sh"]