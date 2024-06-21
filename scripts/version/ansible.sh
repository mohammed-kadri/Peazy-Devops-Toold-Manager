#!/bin/bash

ansible --version | head -n 1 | awk '{print $3}' | sed 's/.$//'
