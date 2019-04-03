#!/bin/sh
set -e

# Start database
sh helm/localdev-db-start.sh

# Setup the database (run migrations)
docker run --rm -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data python manage.py migrate

# Run the application server
docker run -it --rm -p 8000:8000 -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data