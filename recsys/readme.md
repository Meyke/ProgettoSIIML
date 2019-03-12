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

Per analizzare se tutto è funziona correttamente, digitare 
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

### Import Data

```
//per guardare le applicazioni registrate
pio app list

pio-docker import --appid 1 --input data/my_users.json
pio-docker import --appid 1 --input data/my_events.json
pio-docker import --appid 1 --input data/my_events_view.json
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
