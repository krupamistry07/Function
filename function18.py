# What is function?
# A function is a block of code that runs only when it is called.


#Syntax:
# def function_name():
# code
# Ex:
def greet():
    print("Helllo")
greet()

# --------------------------------------------------------------------------------------

# Function with parameters
# Used to pass values
def greet(name):
    print(f"hello {name}")
greet("Krupa")
greet("Shreyarth")
greet("AICW")
# OR
def greet(name="Student"): #by default parameter
    print(f"hello {name}")
greet()
greet("Shreyarth")
greet("AICW")

# --------------------------------------------------------------------------------------

# Function with return value
# Used when we want to send result back
def add(a , b):
    return a + b
result = add(2 , 3)
print(result)

# --------------------------------------------------------------------------------------

# Task 1 - Creat a function calculate and return result.
# Hint : User return statement







# Task 2 - Create a function to cheak if a number is even or odd.
# Hint : Use modulus operator(%)
num = int(input("Enter a Number: "))
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_even_odd(num)
print(result)

# Task 3 - Creat a function to find the factorial of a number.
# Hint : Use a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))
# OR
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
result = factorial(num)
print(result)

# Task 4 - Creat a function to find maximum of three numbers
# hint : user if-else 
# # input - a =  5, b = 10 , c = 3
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a = float(input("Enter a first num: "))
b = float(input("Enter a second num: "))
c = float(input("Enter a third num: "))
result = (find_max(a, b, c))
print(f"The gretest num is: {result}")

# Task 5 - Create a function to cheak if a string is palindrome
# input_str = "madam"
# op : True

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

input_str = input ("Enter a string: ")
result = is_palindrome(input_str)
if result:
    print(f"{input_str} is a palindrome")
else:
    print(f"{input_str} is not a palindrome")

# Task 6 - Create a function to calculate the are of a circle.
def area_of_circle(r):
    return 3.14 * r ** 2

radius = float(input("Enter radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle is:{area}")