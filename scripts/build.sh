#!/bin/bash

set -e

# Build images
docker-compose build --parallel

# Push images
docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
docker-compose push