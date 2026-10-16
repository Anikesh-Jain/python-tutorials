# Write a program that prints all odd numbers from 1 to 20

for i in range(1, 20):
    if(i % 2 != 0):
        print(i)


# Write a program that prints all numbers from 57 to 570 that are divisible by 57

for i in range(57, 571):
    if(i % 57 == 0):
        print(i)


# Write a program that prints all numbers from 1 to 50 that are divisible by 3, except for the number 15

for i in range(1, 50):
    if(i == 15):
        continue
    if(i % 3 == 0):
        print(i)


# Write a program that prints all numbers from 1 to 1000 that are divisible by two numbers entered by the user

a = int(input("Enter first number : "))
b = int(input("Enter last number : "))
for i in range(1, 1000):
    if (i % a == 0 and i % b == 0):
        print(i)
        break