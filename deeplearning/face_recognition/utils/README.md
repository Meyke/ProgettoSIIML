# File di utility

## Descrizione

- Il file create_dataset.py permette di creare un dataset di immagini di attori. Dato un csv con una lista di attori in input scarica una certa quantità(configurabile) di immagini a partire dal nome dell'attore e inserisce queste all'interno della directory downloads/<nome-attore>. Queste immagini a seguito di una processamente ed eventualmente di una revisione possono poi essere al dataset principale nella cartella
- I file change_name.py rinomina le immagini scaricate con il nome dell'attore seguito dal carattere "_" e da un identificatore numerico
- Il file remove_file.py permette di rimuovere in modo automatico una certa quantità di immagini per attore, se si vuole diminuire il numero di immagini disponibili per attore.
- Il file create_list.py crea nella direttori principale una lista di attori a partire dal dataset principale
