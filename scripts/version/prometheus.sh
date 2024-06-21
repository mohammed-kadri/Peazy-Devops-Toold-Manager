#!/bin/bash

prometheus --version 2>&1 | head -n 1 | awk '{print $3}' | sed 's/+.*//'
