import csv

employee = open('employee_data.csv', 'r')

csv_file = csv.reader(employee)

next(csv_file)

for rec in csv_file:
    name = rec[1]
    salary = int(rec[3])
    bonus = salary + float(rec[7])
    pay = salary + bonus

    print(f'Name: {name}')
    print(f'Salary: $ {salary:>.2f}')
    print(f'Bonus: $ {bonus:>.2f}')
    print(f'Pay: $ {pay:>.2f}')

employee.close()


