#!/bin/bash

# Setup script for VM

# Check if script was run with sudo privileges
if [[ $(id -u) -ne 0 ]]; then
  echo "Please run with sudo or as a root." >&2
  exit 1
fi

# Install curl and python virtual environment
apt-get update
apt-get install -y curl python3.11-venv

# Create an environment
python3 -m venv /vagrant/.venv

# Activate the environment
. /vagrant/.venv/bin/activate

# Install requirements.txt
pip install -r /vagrant/requirements.txt

# Quit from a Python virtual environment
deactivate
