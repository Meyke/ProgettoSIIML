import csv
import os
from google_images_download import google_images_download

# nome del file da cui leggere la lista di attori
file_name = "actors_list.csv"

response = google_images_download.googleimagesdownload()

with open(file_name) as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        arguments = {"keywords":row[0],"limit":10,"format":"jpg","size":"medium"}
        response.download(arguments)
