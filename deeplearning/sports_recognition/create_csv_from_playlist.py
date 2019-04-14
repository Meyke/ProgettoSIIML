import pafy
import csv
import os

SEPARATOR=","

with open("videos4.csv", "a") as file:
    writer = csv.writer(file)
    plurl = "https://www.youtube.com/playlist?list=PLLT3ADwEAVXB5e_zNDqBdwiclhhaB8AHf"
    playlist = pafy.get_playlist(plurl)
    for i in range(20):
        url = playlist['items'][i]['pafy'].videoid
        print(url)
        csv_line = "%s%s%s" % ("https://www.youtube.com/watch?v=" + url, SEPARATOR, "cycling")
        writer.writerows([csv_line.split(',')])
