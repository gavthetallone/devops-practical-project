#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-master:
ssh swarm-master << EOF
    sudo usermod -aG docker $USER
    docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
EOF
