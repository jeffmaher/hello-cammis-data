#!/bin/sh
set -e

# Start database
sh helm/localdev-db-start.sh

# sleep here as running the migrate command before the server has finish booting will result in an error
sleep 20

# Setup the database (run migrations)
docker run --rm -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data python manage.py migrate

# Add test data
docker run --rm -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data python manage.py add_test_data

# Run the application server
docker run -it --rm -p 8000:8000 -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data