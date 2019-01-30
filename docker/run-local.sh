#!/bin/sh

docker run -it --rm -p 8000:8000 -v "$(pwd)":"/hello-cammis-data" ca-mmis/hello-cammis-data