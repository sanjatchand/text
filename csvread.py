import csv
def midpoint():
    filename = "D:\Detection_Results.csv"
    fields = []
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    for col in rows[1:2]:
            xmid=(int(col[2])+int(col[4]))/2
            ymid=(int(col[3])+int(col[5]))/2
            return xmid,ymid
x=midpoint()
print(x)
