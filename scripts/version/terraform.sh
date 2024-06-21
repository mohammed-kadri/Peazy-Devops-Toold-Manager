#!/bin/bash

terraform --version | head -1 | awk '{print $2}' | cut -c2-