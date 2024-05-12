#!/bin/bash


install_helm() {
    curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
    # if get_helm.sh is not in the current directory, then exit else execute the script
    if [ ! -f get_helm.sh ]; then
        echo "get_helm.sh not downloaded check your internet or the directory where it's downloaded"
        exit 1
    else
        chmod +x get_helm.sh
        ./get_helm.sh
        rm -f get_helm.sh
    fi
}

install_helm