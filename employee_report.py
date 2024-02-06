import csv

employee = open('employee_data.csv', 'r')

csv_file = csv.reader(employee)

next(csv_file)

