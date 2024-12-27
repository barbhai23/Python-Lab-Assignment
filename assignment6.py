#Assignment 6 
#
#Gayatri Barbhai
#


# Q1 # Write a python program to reverse a number using a while loop. 


num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

print("Reversed number is:", reversed_num)

#Q2. Write a python program to check whether a number is palindrome or not?

num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

if original_num == reversed_num:
    print(f"{original_num} is a Palindrome number.")
else:
    print(f"{original_num} is not a Palindrome number.")

#Q3. Write a python program finding the factorial of a given number using a while loop. 


num = int(input("Enter a number to find its factorial: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is: {factorial}")


#Q4. Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

total = 0

while True:
    num = int(input("Enter a number (enter 0 to stop): "))
    if num == 0:
        break
    total += num

print("The sum of all numbers is:", total)






