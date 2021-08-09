#!/bin/bash

set -e

# Install dependencies
bash scripts/setup.sh

# Run Unit Tests
bash scripts/test.sh

# Build and Push Images
bash scripts/build.sh

# Configure Docker Swarm
bash scripts/config.sh

# Deploy Stack
bash scripts/deploy.sh