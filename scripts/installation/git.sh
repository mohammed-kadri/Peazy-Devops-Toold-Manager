#!/bin/bash

# Git installation
echo "Installing Git..."
sudo apt-get update -y
sudo apt-get install git -y

# Verify Git version
echo "Verifying Git version..."
git --version

# Configure user name and email
read -p "Enter your name: " name
read -p "Enter your email: " email

echo "Configuring Git..."
git config --global user.name "$name"
git config --global user.email "$email"

# Check configurations
echo "Checking Git configurations..."
git config --global --list
