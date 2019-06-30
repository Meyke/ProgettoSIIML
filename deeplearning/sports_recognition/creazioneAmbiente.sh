#!/bin/bash

# OSS: si potrebbe usare docker compose per avere tutti i servizi assieme a PredictionIO
# ma il progetto di deeplearning potrebbe anche girare in un cluster vero e proprio.

# build dell'immagine docker(se si dispone di una macchina con gpu con capabilities maggiori di 3.0 utilizzare come Dockerfile il file dockerfile.gpu). 

docker build -t sports_rec .

# creazione ed esecuzione del contenitore

docker run -it -p 8888:8888 --name=face_rec_cont sports_rec




