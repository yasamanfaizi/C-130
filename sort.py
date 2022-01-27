import csv
df1 = []

with open("unsort.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        df1.append(i) 

h = df1[0]
data = df1[1:]

data.sort(key = lambda data: data[0])

with open("sorteddata.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(h)
    writer.writerows(data)