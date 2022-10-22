import csv

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line[2])

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('newnames.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile, delimiter='-')

        for line in csv_reader:
            csv_writer.writerow(line)

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('newnames.csv', 'w') as newfile:
        csv_writer = csv.writer(newfile, delimiter='\t')

        for line in csv_reader:
            csv_writer.writerow(line)

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for line in csv_reader
        print(line)

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader
        print(line['email'])

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('newnames.csv', 'w') as newfile:
        fieldnames = ['firstname', 'lastname','email']
        csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)

with open('name.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('newnames.csv', 'w') as newfile:
        fieldnames = ['firstname', 'lastname']
        csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)