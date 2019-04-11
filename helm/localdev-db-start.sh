#!/bin/sh
set -e

helm install stable/postgresql --version 3.17 -n hello-cammis-data-postgresql \
    --set global.postgresql.postgresqlDatabase=hellocammisdata \
    --set global.postgresql.postgresqlUsername=hellocammisdata \
    --set global.postgresql.postgresqlPassword=hellocammisdata \
    --set global.postgresql.servicePort=5432 \
    --set persistence.enabled=false \
    --set service.type=LoadBalancer
