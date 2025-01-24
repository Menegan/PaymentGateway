#!/bin/bash
# Set up Python manually if necessary
if ! command -v python &> /dev/null
then
    echo "Installing Python manually..."
    apt-get update
    apt-get install -y python3 python3-pip
fi

# Proceed with the build
python3 -m pip install -r requirements.txt