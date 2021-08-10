#!/bin/bash

rsync -r docker-compose.yaml nginx swarm-master:
ssh swarm-master << EOF
    sudo usermod -aG docker $USER
    docker stack deploy --compose-file docker-compose.yaml pokemon-app
EOF
