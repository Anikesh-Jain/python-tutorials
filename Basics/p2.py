# Write a Python program that takes the prices of three products as input and calculates the total bill amount and the average price. Then, ask the user for their favorite superhero name and print it along with a message indicating whether the name starts with the letter "S" or "s".

p1 = float(input("Enter first product price: "))
p2 = float(input("Enter second product price: "))
p3 = float(input("Enter third product price: "))

total = p1 + p2 + p3
average = total / 3

print("Total bill amount:", total)
print("Average price:", average)


superhero_name = input("Enter your favorite superhero name : ")
print("Your favorite superhero name is :", superhero_name)
print(superhero_name.startswith(("S", "s")))