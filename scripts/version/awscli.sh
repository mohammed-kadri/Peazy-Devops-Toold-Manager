#!/bin/bash

aws --version | grep -o 'aws-cli/[0-9.]*' | awk -F '/' '{print $2}'
