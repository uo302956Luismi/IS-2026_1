#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Uso: ./udp_docker_lanzar_cliente.sh ip_broadcast"
    exit 1
fi

docker run -it --network pruebas \
    -v $(pwd):/app python:3.7 \
    python /app/udp_cliente6_broadcast.py "$1"
