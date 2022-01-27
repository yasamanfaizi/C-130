import csv
df1 = []
df2 = []
with open("dataset_1.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        df1.append(i) 
with open("dataset_2.csv", "r") as f:
    reader = csv.reader(f)
    for i in reader:
        df2.append(i) 
h1 = df1[0]
data1 = df1[1:]

h2 = df2[0]
data2 = df2[1:]

h = h1+h2
data = []
for i, v in enumerate(data1):
    data.append(data1[i]+data2[i])

with open("mergeddata.csv", "a+") as f:
    writer = csv.writer(f)
    writer.writerow(h)
    writer.writerows(data)