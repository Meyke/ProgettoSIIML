#!/bin/bash

# OSS: si potrebbe usare docker compose per avere tutti i servizi assieme a PredictionIO
# ma il progetto di deeplearning potrebbe anche girare in un cluster vero e proprio.

# build dell'immagine. 

docker build -t face_rec_img .

# creazione ed esecuzione del contenitore

docker run -it -p 8888:8888 --name=face_rec_cont face_rec_img




