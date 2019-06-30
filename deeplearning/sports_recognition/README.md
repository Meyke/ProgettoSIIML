# Recognize faces and activity from sports videos.

È stato sviluppato del codice che fa riconoscimento di atleti tramite face recognition e riconoscimento di sport tramite un tool di activity recognition. Per lo sviluppo si è preso in considerazione un dataset di circa 330 video di highlights delle olimpiadi di Rio 2016.
Il codice è presente al seguente notebook da far girare direttamente su Google Colaboratory:
[sport-recognition.ipynb](https://colab.research.google.com/drive/1Ghs_0S0Fbpmb48_zSTrIpXZF82Uldmnj#scrollTo=Zsi_GkHPpCMa).
Per fare face recognition e acctivty recognition sono stati utilizzati i seguenti tool
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [TRN-pytorch](https://github.com/metalbubble/TRN-pytorch/tree/a8e2df8919050b1fa9e94907f71089cd75816c45)

In presenza di una gpu con specifiche adatte sul proprio calcolatore è possibile far girare il codice direttamente sull'apposita  macchina docker ....

In assenza di una gpu adatta, è possibile comunque testare il del sistema facendo esclusivamente face recognition

I file face_encoding e face_recognizer includono il codice per addestrare e fare face_recognition di atleti nell'ambito del dominio dello sport.

Il file sports_recognition è l'equivalente del codice presente nel sopra citato notebook sviluppato su colab che permette di fare sia face recognition che activity recognition, qualora si disponga sulla propria macchina di una gpu con specifiche adatte.

Il file sports-recognition_test è stato utilizzato per effetuare dei test a partire dalla lista di video specificata nel file videos.csv

## ALTRO

- I file athletes_embedding.csv e atheletes_metadata.csv contengono rispettivamente i face embedding di atleti presi da un dataset di 242 atleti e i corrispondenti metadati.
- I file sports1.csv e sports2.csv contengono il mapping tra attività e sport.
- Il file videos.csv contiene i video utilizzati per il test del tool.
