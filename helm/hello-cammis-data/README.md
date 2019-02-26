# hello-cammis-data-helm

Helm Chart for deploying [hello-cammis-data](https://github.com/ca-mmis/hello-cammis-data) to a Kubernetes cluster.

## Setup Instructions

### Dependencies

- Kubernetes Cluster
- Tiller installed into your Kubernetes Cluster
- Helm configured to Tiller in your Kubernetes Cluster

### Steps

1. Navigate into the base of this directory via a terminal
1. Get dependencies: `helm dep up .`
1. Deploy (Kubernetes Deployment and Service): `helm install . -n hello-cammis-data`
1. Verify:
    - `helm ls`
    - `kubectl get all`
    - Go to: `http://<cluster url>:8000` (get this via `kubectl get svc`)
1. Delete: `helm delete --purge hello-cammis-data`
