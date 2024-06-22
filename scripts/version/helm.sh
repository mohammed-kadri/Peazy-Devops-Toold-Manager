#!/bin/bash

helm version --short | sed 's/^v//' | sed 's/+.*//'