import csv

print("Scanning processed users - start")

with open('data.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    processed_nodes = {row[0] for row in reader}
print("Scanning processed users - end")

with open('data.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')
    i = 1
    with open('data_reduced3.csv', 'w') as f:
        for row in reader:
            i += 1
            if i % 1000 == 0:
                print("Processed {} users".format(i))
            followers = [f for f in row[2].split(',') if f in processed_nodes]
            f.write("{};{};{}\n".format(row[0], row[1], ','.join(followers)))
