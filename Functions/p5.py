# WAF to check if a number is even or odd 

def check_even_odd(n):
    # n = int(input("Enter the number : "))
    if n % 2 == 0:
        print("The number is even")

    else: 
        print("The number is odd")    

check_even_odd(10)      


# WAF to count the number of vowels in th string

def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Anikesh"))


# WAF to check if a number is prime or not 

def check_prime(n):
    if n<=1:
        print("The Number is not Prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("The Number is not Prime") 
            return

    print("The Number is Prime")  

check_prime(11) 


# WAF to return the average marks if a list of marks is passed as parameter

def avg_marks(marks):
    total = 0

    for i in marks:
        total = total + i

    avg = total / len(marks)

    print("The average of the marks is:", avg)


avg_marks([1, 2, 3, 4, 5])