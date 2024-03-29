# hello-cammis-data

An application used to test data change deployments and connect to an app that consumes this API.

## Developer Setup

### Dependencies

- Docker CE 18.x ([Mac/Win](https://www.docker.com/products/docker-engine), [Linux](https://hub.docker.com/search/?offering=community&operating_system=linux&platform=server&q=&type=edition))
- A local Kubernetes cluster (recommendation: use the one built into Docker CE)
- Helm (configured to connect to the local Kubernetes cluster)
- Windows only: A Linux-like terminal, such as [Ubuntu for Windows](https://www.microsoft.com/en-us/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab)

### Instructions

This launches a Linux terminal for doing development on the app. When the server is running, port `8000` is exposed to the developer's host machine (i.e. `http://localhost:8000/` is the base address).

1. Start Docker
1. Clone this repo
1. Navigate into its base directory via a terminal
1. Build the Docker image: `sh docker/build-local.sh`
1. Launch a terminal/Docker instance: `sh docker/bash-local.sh`
1. (First time only:) Create the database file: `python manage.py migrate`
1. (First time only:) Load test data: `python manage.py add_test_data`
1. Run the server: `python manage.py runserver 0.0.0.0:8000`

To exit out:

1. CTRL+C to exit the Python/Django process
1. Type `exit` to exit the Docker terminal session
1. Run `sh helm/localdev-db-stop.sh` to stop the database

## Running w/ Docker Locally

This assumes the database has already been setup/migrated.

1. Run the application: `sh docker/run-local.sh`
1. Visit any of the endpoints listed below via HTTP

## Endpoints

### Hello (GET): `http://(address):8000/hello/<name>`

Returns a JSON payload with that looks like:

`{"hello": "(some message)"}`

This returns a HTTP 404 if a greeting for the name hasn't been loaded.

Example (`/hello/dave`):

`{"hello": "Yo Dave!"}`

### Add Greeting (POST): `http://(address):8000/add_greeting/<name>`

As a POST command, also requires the following form-data:

- `greeting`: A string message that will greet someone with the `<name>` in the URL.

Example (`/add_greeting/dave`) with form-data as `greeting` --> `"Yo Dave!"`:

`{"name": "dave", "greeting": "Yo Dave!"}`

_Note: [Postman](https://www.getpostman.com) or `curl` are good ways to try this._

### App is Working Internally (GET): `http://(address):8000/alive`

Sends an HTTP code to indicate that the application itself is healthy. This doesn't mean it's ready for traffic, but that everything in the application is functioning as expected.

Designed to be plugged into a Kubernetes liveliness probe.

### Ready for Traffic / Dependencies Up (GET): `http://(address):8000/ready`

Sends an HTTP code to indicate that the application can safely receive traffic. This is an indication that both the application itself is healthy and that external dependencies, such as the database, are functioning.

Designed to be plugged into a Kubernetes readiness probe.

## Database Migrations

Here's directions to try out a roll forward and a roll back locally.

## Roll Forward

This migration is on the Greeting model, which has the following fields at the start:

- `name`
- `greeting`

The migration removes the last character from the greeting and places it into a punctuation column, leaving the Greeting model with following fields:

- `name`
- `greeting`
- `punctuation`

1. Clone this repo
1. Switch to tag `2.0.0`
1. [Do the normal setup steps](#instructions), minus starting the server
1. Add test data: `python manage.py add_test_data`
1. Inspect the database at `hellocammisdata.public.data_greeting`
1. Switch the tag to `2.1.0`
1. Run the migration: `python manage.py migrate data`
1. Inspect the database at `hellocammisdata.public.data_greeting`. Note that the last character punctuation has been split into a new column

## Rollback

This reverses the roll forward operation we just did, and should be done immediately after the above steps.

1. Show the migrations for the `data` module: `python manage.py showmigrations data`
1. Revert the migration to an older state: `python manage.py migrate data 0004`
1. Inspect the database at `hellocammisdata.public.data_greeting`. Note that the model has been returned to its `2.0.0` state.
1. (Optional) If you switch the tag back to `2.0.0`, the application will run in its prior state.
