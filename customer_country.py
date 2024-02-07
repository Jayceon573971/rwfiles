import csv


infile = open('customers.csv', 'r')

csv_file = csv.reader(infile)

next(csv_file)

outfile = open('customer_country.csv', 'w')

outfile.write("Full Name, Country" + "\n")

for rec in csv_file:
    full_name = rec[1] + " " + rec[2]
    country = rec[4]
    outfile.write(full_name + ", " + country + "\n")

infile.close()
outfile.close()

