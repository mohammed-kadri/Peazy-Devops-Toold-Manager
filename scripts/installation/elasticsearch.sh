#!/bin/bash

# Update package lists
sudo apt-get update

# Install required packages
sudo apt-get install -y apt-transport-https openjdk-11-jre-headless uuid-runtime pwgen

# Import Elasticsearch GPG key
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

# Add Elasticsearch repository
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list

# Update package lists again
sudo apt-get update

# Install Elasticsearch
sudo apt-get install -y elasticsearch

# Enable and start Elasticsearch service
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch

# Set elastic user password
ES_PASSWORD=$(pwgen 15 1)
echo "Elasticsearch password: $ES_PASSWORD"
echo "$ES_PASSWORD" | sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic -i

# Configure Elasticsearch to start automatically on system boot
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch.service

echo "Elasticsearch installed and started successfully!"