#Q1. Print the table of 5 using for loop
print("Table of 5:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


#Q2. Print even number series by taking input from the user:
n = int(input("Enter the range for even numbers: "))
print("Even numbers are:")
for i in range(2, n+1, 2):
    print(i, end=" ")


#Q3. Create a list and iterate through its items using a for loop:
fruits = ["mango", "orange", "grapes", "pineapple"]
print("\nList of fruits:")
for fruit in fruits:
    print(fruit)


#Q4. Calculate the sum of numbers from 1 to 10:
total = 0
for i in range(1, 11):
    total += i
print("Sum of numbers from 1 to 10 is:", total)


#Q5. Print the pyramid pattern:
rows = 5
for i in range(rows):
    print(' ' * (rows - i - 1) + '*' * (2 * i + 1))


#Q6. Print the first 10 natural numbers using for loop:
print("First 10 natural numbers:")
for i in range(1, 11):
    print(i, end=" ")


#Q7. Python program to check if the given string is a palindrome:
text = input("\nEnter a string (e.g., 'radar' or 'level'): ").lower()
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#Q8. Python program to check if a given number is an Armstrong number:
num = int(input("Enter a number (e.g., 153 or 9474): "))
sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


#Q9. Python program to get the Fibonacci series between 0 to 50:
a, b = 0, 1
print("Fibonacci series between 0 and 50:")
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b


#Q10. Python program to check the validity of password input by users:
import re

password = input("\nEnter your password (e.g., 'Secure@1234'): ")

if (len(password) >= 8 and
    re.search(r'[A-Z]', password) and
    re.search(r'[a-z]', password) and
    re.search(r'\d', password) and
    re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
    print("Valid Password")
else:
    print("Invalid Password. Ensure it meets the following criteria:")
    print("1. At least 8 characters long")
    print("2. Contains at least one uppercase letter (A-Z)")
    print("3. Contains at least one lowercase letter (a-z)")
    print("4. Contains at least one digit (0-9)")
    print("5. Contains at least one special character (!@#$%^&*(),.?\":{}|<>)")
