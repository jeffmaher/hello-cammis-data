#!/bin/sh

# Start the database
sh helm/localdev-db-start.sh

# Run a Bash Terminal within the container
docker run -it --rm -p 8000:8000 -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data bash