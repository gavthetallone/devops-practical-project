#!/bin/bash

rsync -r docker-compose.yaml swarm-master:
rsync -r nginx_lb/nginx.conf remote:~/nginx/ swarm-master:
ssh swarm-master << EOF
    sudo usermod -aG docker $USER
    docker login -u ${DOCKER_CREDENTIALS_USR} -p ${DOCKER_CREDENTIALS_PSW}
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
EOF
