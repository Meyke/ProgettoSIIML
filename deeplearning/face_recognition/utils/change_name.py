import os

for dirname, dirnames, filenames in os.walk("athletes"):
    for subdirname in dirnames:
        subject_path = os.path.join(dirname, subdirname)
        counter = 1
        for filename in os.listdir(subject_path):
            os.rename(subject_path + "/" + filename, subject_path + "/" + subdirname + "_" + str(counter) + ".jpg")
            counter += 1
