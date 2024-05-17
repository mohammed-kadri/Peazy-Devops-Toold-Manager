#!/bin/bash

# Update package lists
sudo apt-get update

# Install required packages
sudo apt-get install -y wget gnupg2

# Import Prometheus GPG key
wget -qO - https://repos.influxdata.com/influxdb.key | sudo apt-key add -

# Add Prometheus repository
echo "deb https://repos.influxdata.com/ubuntu bionic stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

# Update package lists again
sudo apt-get update

# Install Prometheus
sudo apt-get install -y prometheus

# Enable and start Prometheus service
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus

echo "Prometheus installed and started successfully!"
