import pafy
import csv
import os

SEPARATOR=","

with open("videos.csv", "a") as file:
    writer = csv.writer(file)
    plurl = "https://www.youtube.com/playlist?list=PLz-gfY4so9kYXI5pYbwD5CxuFAPw97-V6"
    playlist = pafy.get_playlist(plurl)
    for i in range(20):
        url = playlist['items'][i]['pafy'].videoid
        print(url)
        csv_line = "%s%s%s" % ("https://www.youtube.com/watch?v=" + url, SEPARATOR, "athletics")
        writer.writerows([csv_line.split(',')])
