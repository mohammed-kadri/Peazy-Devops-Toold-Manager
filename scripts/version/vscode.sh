#!/bin/bash

dpkg -l code | awk '/^ii/ { split($3, version, "-"); print version[1] }'