#!/usr/bin/env bash

OPT=$1

function black() {
  docker-compose run --rm introcs bash -c "black ."
}

function ex() {
  docker-compose run --rm introcs bash -c "python -m $1"
}

function help() {
  echo "help
  - black : code lint
  - ex: exec python code
    example: ./dev.sh ex \"introcs.xxx.file_name\"
  "
}

case $OPT in
black)
  black
  ;;
ex)
  ex "$2"
  ;;
*)
  help
  ;;
esac
