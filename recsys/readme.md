# Recommender

Tale progetto è basato sul template *SimilarProduct* cui descrizione può essere trovata sul sito di [PredictionIO](https://predictionio.apache.org/templates/similarproduct/quickstart/)

Tale engine raccomanda prodotti che sono "simili" al prodotto passato nella query. La similarità non è definita dagli attributi
degli items o degli users, ma dalle azioni svolte in passato dagli utenti. Di default, esso usa l'evento "view" tale che i prodotti
A e B sono considerati simili se la maggior parte che ha visto A ha anche visto B.<br>
Tale template può essere modificato per supportare altre azioni, come *buy*, *rate*, *like*, ... etc. 

### Prerequisiti

L'unica cosa che si richiede che venga installato sul proprio pc è [Docker](https://www.docker.com/).

### Installazione e avvio dell'ambiente

Il seguente script avvia PredictionIO con un event server. L'immagine docker di PredictionIO monta la directory ./templates in /templates.

```
chmod 777 avvioAmbiente.sh 
./avvioAmbiente.sh
```

Per analizzare se tutto funziona correttamente, digitare 
```
$ pio-docker status
...
[INFO] [Management$] Your system is all ready to go.
```

Per registrare l'applicazione, digitare:

```
chmod 777 registraApp.sh
./registraApp.sh
```

Per guardare quali sono le applicazioni registrate nel server

```
pio-docker app list
```
### Import Data

Per importare i dati in batch:

```
// Attenzione: modificare opportunamente <APP_ID> in
// pio-docker import --appid <APP_ID> --input data/my_users.json

chmod 777 import_data.sh
./import_data.sh
```

### Train del modello e deploy

```
chmod 777 train_and_deploy.sh
./train_and_deploy.sh
```

Il modello sarà in ascolto sulla porta 8000

## Lanciare Query (da togliere)

```
example
```

