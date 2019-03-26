import csv
import os

with open("../list.csv", "w") as file:
    writer = csv.writer(file, delimiter=',')
    for dirname, dirnames, filenames in os.walk("../dataset"):
        for subdirname in dirnames:
            writer.writerow([subdirname])
