# q1

roll_no = [101, 105, 102, 101, 108, 105, 110]
unique_roll_no = list(set(roll_no))
print(unique_roll_no)

# q2

info = [
    (101, "Alice", 50000),
    (102, "Bob", 650000),
    (103, "Charlie", 45000)
]

Employee_ID = int(input("Enter your employee id :"))

for employee in info:
    if employee[0] == Employee_ID:
        print("Employee ID is :" , employee[0])
        print("Employee Name is :" , employee[1])
        print("Employee Salary is :" , employee[2])
        break

    
    else:
        print("Employee is not found")
