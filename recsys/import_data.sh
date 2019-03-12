#!/bin/bash

DIRECTORY='predictionio/docker/'
if [ -d "$DIRECTORY" ]; then
  cd predictionio/docker/templates/MyRecommendation
  # pio-docker import --appid <app_id> --input data/my_users.json
  pio-docker import --appid 1 --input data/my_users.json
  pio-docker import --appid 1 --input data/my_events.json
  pio-docker import --appid 1 --input data/my_events_view.json
else
	echo "devi scaricarti prima predictionIO"
fi

# build del modello
pio-docker build --verbose

