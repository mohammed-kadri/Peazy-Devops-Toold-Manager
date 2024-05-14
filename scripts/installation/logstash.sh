#!/bin/bash

# Add Elastic's signing key
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg

# Install prerequisite
sudo apt-get install apt-transport-https

# Save the repository definition
echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-8.x.list

# Update package lists
sudo apt-get update

# Install Logstash
sudo apt-get install logstash
