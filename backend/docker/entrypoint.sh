#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

export DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"

postgres_ready() {
python << END
import sys
import time
import psycopg2
suggest_unrecoverable_after = 30
start = time.time()
while True:
    try:
        psycopg2.connect(
            dbname="${POSTGRES_DB}",
            user="${POSTGRES_USER}",
            password="${POSTGRES_PASSWORD}",
            host="${POSTGRES_HOST}",
            port="${POSTGRES_PORT}",
        )
        break
    except psycopg2.OperationalError as error:
        sys.stderr.write("Waiting for PostgreSQL to become available...\n")
        if time.time() - start > suggest_unrecoverable_after:
            sys.stderr.write("  This is taking longer than expected. The following exception may be indicative of an unrecoverable error: '{}'\n".format(error))
    time.sleep(1)
END
}

timeout=30
start_time=$(date +%s)
while ! postgres_ready; do
    current_time=$(date +%s)
    elapsed_time=$(( current_time - start_time ))
    if (( elapsed_time > timeout )); then
        echo "PostgreSQL is not available after ${timeout} seconds. Exiting."
        exit 1
    fi
    echo "Waiting for PostgreSQL (${elapsed_time}s elapsed)..."
    sleep 1
done

echo "PostgreSQL is available."

exec "$@"