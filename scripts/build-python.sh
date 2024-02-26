#!/bin/bash

DOCKER_BASE=$(dirname "$(realpath "${BASH_SOURCE[0]}")")/..

./scripts/build-docker.sh

# If we don't do this, we'll end up with files owned by root
# all over the place.
export USER_ID=$(id -u)
export GID=$(id -g)

docker run -it --rm \
    -v $(pwd):/calico:rw \
    ghcr.io/yangjames/calico:latest \
    /bin/bash 