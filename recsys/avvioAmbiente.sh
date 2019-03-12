#!/bin/bash

#scarica PredictionIO

DIRECTORY='predictionio/docker/'
if [ ! -d "$DIRECTORY" ]; then
  git clone https://github.com/apache/predictionio.git
  cd predictionio/docker
  $ export PATH=`pwd`/bin:$PATH
  echo "predictionio scaricato"
fi


docker-compose -f docker-compose.yml \
  -f pgsql/docker-compose.base.yml \
  -f pgsql/docker-compose.meta.yml \
  -f pgsql/docker-compose.event.yml \
  -f pgsql/docker-compose.model.yml \
  up
