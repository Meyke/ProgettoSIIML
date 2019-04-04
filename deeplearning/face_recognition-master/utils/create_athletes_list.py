import csv

with open('athletes_list.csv', mode='w') as file:
    csv_writer = csv.writer(file, delimiter=',')
    with open('athletes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[8] != str(0) or row[9] != str(0) or row[10] != str(0):
                csv_writer.writerow([row[1]])



