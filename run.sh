#!/bin/bash

sleep_delay=5

docker-compose up -d --build
sleep $sleep_delay
docker exec -it python bash
