#!/bin/bash

rsync -r docker-compose.yaml nginx/nginx.conf swarm-master:

ssh swarm-master << EOF
    export DATABASE_URI=${DATABASE_URI}
    export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
    export MYSQL_DATABASE=${MYSQL_DATABASE}
    sudo usermod -aG docker $USER
    docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
EOF
