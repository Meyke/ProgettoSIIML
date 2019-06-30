# ProgettoSIIML
Progetto per il corso di SII e ML


## Creazione della rete (solo dopo aver avviato tutti i contenitori...andare nelle directory di interesse per avviarli)

Per analizzare quali reti ho, digitare

```
docker network ls
```

```
docker network create SII_network

docker network inspect SII_network

docker network connect SII_network sports_rec

docker network connect SII_network docker_pio_1
```

se il contenitore è avviato, per ottenere il suo ip:

```
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <name or id container>

```

## Dominio dei trailer di film

Il sistema di raccomandazione è predisposto per il dominio dei video di sport. Se si vuole testare il tool che fa face recognition sugli attori andare nell'apposita sottodirecotry e seguire le istruzioni per eseguire il codice sull'apposita macchina docker.


