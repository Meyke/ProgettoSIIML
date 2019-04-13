import pafy
import csv
import os

SEPARATOR=","

with open("videos.csv", "a") as file:
    writer = csv.writer(file)
    plurl = "https://www.youtube.com/playlist?list=PL-292yfpAFGb4_xI5kzFMppiv915n_FQI"
    playlist = pafy.get_playlist(plurl)
    for i in range(12):
        url = playlist['items'][i]['pafy'].videoid
        print(url)
        csv_line = "%s%s%s" % ("https://www.youtube.com/watch?v=" + url, SEPARATOR, "fencing")
        writer.writerows([csv_line.split(',')])
