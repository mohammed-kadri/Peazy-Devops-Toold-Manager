#!/bin/bash

docker --version | awk '{print $3}' | sed 's/,//'
