num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
operator = input("Enter the operator : ")

if(operator == "+"):
    sum = num1 + num2
    print("The sum is :",sum)
elif(operator == "-"):
    sub = num1 - num2
    print("The difference is :",sub)
elif(operator == "*"):
    prod = num1 * num2
    print("The product is :",prod)
elif(operator == "/"):
    div = num1 / num2
    print("The division is :",div)
elif(operator == "%"):
    mod = num1 % num2
    print("The modulus is :",mod)
elif(operator == "**"):
    expo = num1 ** num2
    print("The exponent is :",expo)
else:
    print("Invalid operator")