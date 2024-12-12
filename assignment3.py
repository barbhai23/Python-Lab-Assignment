
# Name:Gayatri Barbhai 
# Python Assignment-3


# Q.1) Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

num = int(input("Enter a number: "))

if num % 2 == 0:
	print("It is an Even Number")
else:
	print("It is odd number")

Output: 
Enter a number: 2
It is an Even Number

Enter a number: 7
It is odd number


# Q.2. Using input function take two number and then swap the number 

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("Before Swapping: num1 = ", num1, "num2 = ", num2)
num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("After Swapping: num1 = ", num1, "num2 = ", num2)

Output:
Enter 1st number: 10
Enter 2nd number: 8
Before Swapping: num1 = 10.0 num2 = 8.0
After Swapping: num1 = 8.0 num2 = 10.0



# Q.3 Write a Program to Convert Kilometers to Miles

kilometer_input = float(input("Enter value in kilometer: "))

conv_fact = 0.621371

miles = kilometer_input * conv_fact

print(kilometer_input, "kilometer is equal to", round(miles,2),"miles")


Output:
Enter value in kilometer: 14
3.5 kilometer is equal to 8.70 miles


# Q.4) Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

principal = 200	# Principal amount in Rs.
rate = 5	# Rate of interest per year in percent
time = 5	# Time period in years

simple_interest = (principal * rate * time) / 100

print("The simple interst on Rs", principal,"is: ", simple_interest)

Output:
The simple interest on Rs 800 is: 40.0
