import cv2
import os
import pafy
import csv

SEPARATOR=","

with open('videos.csv') as csv_file:
    with open("dataset.csv", "w") as file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        counter = 0

        for row in csv_reader:
            url = row[0]
            label = row[1]
            vPafy = pafy.new(url)
            play = vPafy.getbest()
            video = play.download()


            # Open the input movie file
            input_movie = cv2.VideoCapture(video)
            length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

            frame_number = 0

            current_path = os.getcwd()

            counter1 = 0

            os.makedirs("dataset/" + str(counter))

            while True:
                # Grab a single frame of video
                ret, frame = input_movie.read()
                frame_number += 1

                # Quit when the input video file ends
                if not ret:
                    break


                cv2.imwrite(current_path + "/dataset/" + str(counter) + "/image"+str(counter1)+".jpg",frame)
                counter1 = counter1 + 1


                print("Writing frame {} / {}".format(frame_number, length))

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # All done!
            input_movie.release()
            cv2.destroyAllWindows()
            print(row[0] + " completed")

            writer = csv.writer(file)
            csv_line = "%d%s%s" % (counter, SEPARATOR , label)
            writer.writerows([csv_line.split(',')])

            counter = counter + 1

print("Finito")

