#!/bin/bash

DOCKER_PASSWORD=$( cat ../secrets/DOCKER_PASSWORD )
DOCKER_PASSWORD=$DOCKER_PASSWORD python3 ./cd-tools.py
