# ProgettoSIIML
Progetto per il corso di SII e ML

### TO do
* inserire uno script per la creazione di una rete bridge docker (vedi sotto cosa scrivere);
* citare le fonti del progetto in Scala (SimilarProduct);
* modificare l'output restituito dal face-recognition. Deve restituire un json fatto in un particolare modo.
* creazione di un unico script globale che fa eseguire gli script di creazione dell'ambiente in un certo ordine (optional)


## Creazione della rete (solo dopo aver avviato tutti i contenitori)

Per analizzare quali reti ho, digitare

```
docker network ls
```

```
docker network create SII_network

docker network inspect SII_network

docker network connect SII_network face_rec_cont

docker network connect SII_network docker_pio_1
```

se il contenitore è avviato, per ottenere il suo ip:

```
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <name or id container>

```
