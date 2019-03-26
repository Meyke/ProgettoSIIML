import os

# Numero di immagini per attore che si vuole mantenere
images_per_actor = 5

for dirname, dirnames, filenames in os.walk("downloads"):
    for subdirname in dirnames:
        subject_path = os.path.join(dirname, subdirname)
        print(subject_path)
        counter = 1
        for filename in os.listdir(subject_path):
            print(counter)
            if(counter > images_per_actor):
                os.remove(subject_path + "/" + subdirname + "_" + str(counter) + ".jpg")
            counter = counter + 1
