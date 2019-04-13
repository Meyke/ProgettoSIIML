import pafy
import csv
import os

SEPARATOR=","

with open("videos.csv", "a") as file:
    writer = csv.writer(file)
    plurl = "https://www.youtube.com/playlist?list=PLQrUWi5X12Nm0ZZvuiYN0dIReOJh1TJF6"
    playlist = pafy.get_playlist(plurl)
    for i in range(20):
        url = playlist['items'][i]['pafy'].videoid
        print(url)
        csv_line = "%s%s%s" % ("https://www.youtube.com/watch?v=" + url, SEPARATOR, "rowing")
        writer.writerows([csv_line.split(',')])
