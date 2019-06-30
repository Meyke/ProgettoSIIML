#!/bin/bash

DIRECTORY='predictionio/docker/'
if [ -d "$DIRECTORY" ]; then
  cp -R recommender/ predictionio/docker/templates/MyRecommendation
  export PATH=`pwd`/predictionio/docker/bin:$PATH
  cd predictionio/docker/templates/MyRecommendation
  pio-docker app new SII
else
	echo "devi scaricarti prima predictionIO"
fi
