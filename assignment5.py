
# Name: gayatri barbhai
# Python Assignment-5


# Q.1) Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

def div(a,b):
	return a/b
	

num1 = 80
num2 = 5

print("Division of", num1, "and", num2, "is", (div(num1,num2)))

Output:
Division of 80 and 5 is 16.0




# Q.2) Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number . 

def square(num):
	return num * num

num = 5

print("Square: ", square(num))

Output:
Square:  25




# Q.3) Using max() and min() functions display the maximum and minimum of 5 random numbers. 

import random

def find_max_min():
    # Generate 5 random numbers between 1 and 100
    numbers = [random.randint(1, 100) for _ in range(5)]
    
    # Display the random numbers
    print("Random numbers:", numbers)
    
    # Find and display the maximum and minimum numbers
    print("Maximum number:", max(numbers))
    print("Minimum number:", min(numbers))

# Call the function
find_max_min()

Output:
Random numbers: [20, 40, 70, 90, 50]
Maximum number: 90
Minimum number: 20



# Q.4) Accept a name from the user and display that in lower case using lower() function

def lowercase():
	name = input("Enter name: ")
	lowercase_name = name.lower()

	print("Name in lowercase = ", lowercase_name)	

lowercase()


Output:

Enter name: GAYATRI BARBHAI
Name in lowercase =  gayatri barbhai