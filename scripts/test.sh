#!/bin/bash

set -e

# Install Dependencies
sudo apt-get update > /dev/null
sudo apt-get install python3 python3-venv -y > /dev/null

# Install Pip Requirements
python3 -m venv venv && source venv/bin/activate
pip3 install --upgrade pip
pip3 install --upgrade setuptools

for i in {1..4}; do pip3 install -r service_${i}/requirements.txt > /dev/null; done

# Unit Testing
python3 -m pytest --cov --cov-config=.coveragerc --cov-report xml --junitxml junit.xml
