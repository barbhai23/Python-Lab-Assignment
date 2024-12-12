#Assignment 1 

Q.1 Print Helloworld
Input- 
print("Hello World")
output-
Hello World

Q.2 Describe Local Variable And Global Variable Code
Input - 
x = 10
def my_function():
    # Local variable
    y = 5
    print("Local variable y:", y)
    print("Global variable x:", x)
my_function()

Output- 
Local variable y: 5
Global variable x: 10

Q.3 Write A Code That Describe Indentation Error
def my_function():
print("Hello, World!")  # This will cause an indentation error

my_function()

output:
print("Hello, World!")  # This will cause an indentation error
    ^
IndentationError: expected an indented block after function definition on line 3

Q.4 Write A Code That Describe Local And Global Variable With Same Name
Input-
X=10
def main():
    X=30
    print ('X=',X)

def globalvar():
    global X
   
    print ('X',X)
main()
globalvar()

Output:

X= 40
X 10

Q.WAPP to print Write a code for string, int and float input.

INPUT-
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("Your name is:", name)
print("Your age is:", age)
print("Your height is:", height)


OUTPUT-
Enter your name: John
name is: John
Enter your age: 25
age is: 25
Enter your height in meters: 1.75
height is: 1.75