# Recognize Images From Video

### Installazione e avvio dell'ambiente

Il seguente script avvia un contenitore in cui è installato un notebook per sviluppare ed eseguire eventuali test. Per avviare il contenitore eseguire lo script:

```
chmod 777 creazioneAmbiente.sh 
./creazioneAmbiente.sh
```

E' possibile accedere al notebook o tramite il link che viene indicato dal terminale, oppure direttamente nel proprio browser preferito immettere:

```
http://127.0.0.1:8888/tree
```

### comandi utili 

Per stoppare (attenzione, non rimuovere) il contenitore con nome *face_rec_cont*:

```
docker stop face_rec_cont
```
Per avviare il contenitore in modo interattivo:

```
docker start -i face_rec_cont
```

**ATTENZIONE**: se eliminiamo un contenitore, viene eliminato anche il suo contenuto. Questo può essere evitato montando un VOLUME linkato con qualche cartella del proprio host. Si guardi la documentazione di docker.

## ALTRO

- Il file face_encoding.ipynb contiene il codice che è stato per l'addestramento(da non utilizzare)
- I file embedding.csv e metadata.csv contengono gli embedding che sono stati addestrati dal dataset di 217 attori e una mappa utilizzata per l'etichettatura delle facce.
- Il file list.csv contiente la lista degli attori contenuti nel dataset
