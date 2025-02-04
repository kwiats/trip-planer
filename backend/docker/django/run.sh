#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# exits if any of your variables is not set
set -o nounset

# It's okay to run the following two, flush and migrate commands on development mode (when debug mode is on) but not recommended
# for production:
if [ "${ENVIRONMENT:-development}" == "development" ]; then
    python manage.py flush --no-input
    python manage.py migrate
fi

# Run the Django development server
python manage.py runserver 0.0.0.0:8000

exec "$@"
