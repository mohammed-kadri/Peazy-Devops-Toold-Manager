#!/bin/bash

UB(){
    # check if docker is already installed
    if (ls /bin | grep "docker" >/dev/null); then
        echo "Docker is already installed"
        read -p "Do you want to uninstall previous docker version? (y/n) " check_ans
        if [ "$check_ans" = "y" ]; then
            sudo apt-get remove docker docker-engine docker.io containerd runc
            sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin
            sudo apt-get autoremove --purge docker-ce docker-ce-cli containerd.io docker-compose-plugin
        else
            echo "skipping uninstallation of previous docker version"
            exit
        fi
    fi
    # 1. Set up the repository
    sudo apt-get update
    sudo apt-get install -y \
        ca-certificates \
        curl \
        gnupg \
        lsb-release

    sudo mkdir -p /etc/apt/keyrings
    sudo rm -f /etc/apt/keyrings/docker.gpg
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

    # add docker repository to apt source list
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    # 2. Install Docker Engine
    sudo apt-get update
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    sudo apt-get update

    # 3. Install Docker Engine, containerd, and Docker Compose.
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
}

UB
