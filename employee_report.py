high_eff = []
low_eff = []
age_40s = []
age_30s = []
age_20s = []

import csv

csv_file = open('employee_data.csv', 'r')

report = csv.reader(csv_file)

next(report)

for record in report:
    name = record[1]
    age = int(record[2])
    productivity = int(record[5])
    hours_worked = int(record[4])
    efficiency_factor = productivity / hours_worked
    if efficiency_factor > 2:
        high_eff.append(name)
    elif efficiency_factor < 1:
        low_eff.append(name)
    if 40 <= age < 50:
        age_40s.append(name)
    elif 30 <= age < 40:
        age_30s.append(name)
    elif 20 <= age < 30:
        age_20s.append(name)

csv_file.close()

print("Highly Efficient Individuals:")
for selec in high_eff:
    print(selec)

print("\nLow Efficient Individuals:")
for selec in low_eff:
    print(selec)

print("\nEmployees in their 40s:")

for selec in age_40s:
    print(selec)
print(f"Total number of employees in their 40s: {len(age_40s)}")

print("\nEmployees in their 30s:")
for selec in age_30s:
    print(selec)
print(f"Total number of employees in their 30s: {len(age_30s)}")

print("\nEmployees in their 20s:")
for selec in age_20s:
    print(selec)
print(f"Total number of employees in their 20s: {len(age_20s)}")

