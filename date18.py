# What is loop?
# A loop is used torepeat a block of code multiple times until a condition is met.

# Types of loop in python
# 1. For loop - Used when we know many times we want to repeat.
# Syntax: 
# for variable in sequence:
# code
# Range() function is commonly userd to generate a sequence of number.
# range comes with 3 parameters:
# 1.start(inclusive)
# 2.stop(exclusive)
# 3.step(optional , default is 1)
# range(start , stop-1 ,step)
# Example-
# for i in range(1 , 6):
#     print(i)
# op : 1 2 3 4 5

# # Key points:
# # 1.range(start,step)generates numbers
# # 2.Loop runs fixed number of times

# # --------------------------------------------------------------------------------------

# # 2.While loop  - Used when we repeat until a condition becomes False
# # Syntax:
# # while condition:
# #     code

# i = 1
# while i <= 5:
#     print(i)
#     i += 1 
#op:1 2 3 4 5

# # Loop control Statement

# # 1.Break - Stop the loop immediately 
# # Example
# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)
#op:1 2

# # 2. Continue - Skip current iteration 
# # Example
# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i) 
#op:1 2 4 5

# # Pass - Does nothing(placeholder)
# for i in range(5):
#    pass 
#op:1 2 3 4 5 

# # Task 1 - Print numbers from 1 to 10 using for loop.
# for i in range(1 , 11):
#     print(i)

# # Task 2 - Print even number from 1 to 20.
# # for i in range(2, 21):
#     if i % 2 == 0:
#         print(i, end = ' ')
# # ---------OR-------------
# for i in range(2, 21 ,2):
#         print(i, end = ' ') 
#op: 2 4 6 8 10 12 14 16 18 20

# # Task 3 - Print odd number from  1 to 15.
# for i in range(1, 21 ,2):
        # print(i, end = ' ') 
#op: 1 3 5 7 9 11 13 15

# Task 4 - Print each character of string.
# text = "Python"
# for i in text:
#      print(i)
# op:P
#    y
#    t
#    h
#    o
#    n

# Task 5 - Print all items in the list.
# data = ["Data","Science","AI"]
# for item in data:
#      print(item) 
#op: Data Science AI
    
# Task 6 - Find some of number 1 to 10.
# total = 0
# for i in range(1, 11):
#     total += i
# print(total)     # total of 1 to 10
# op: 55

# Task 7 - Print multiplication table of 5.
# for i in range(1, 11):
#     print(f"5 x {i} = {5 * i}")
# op: 5 x 1 = 5 -------------------------

# Task 8 - Count how many vowels are in a string.
# text = "Hello World"
# count = 0
# for char in text.lower():
#     if char in "aeiou":
#         count += 1
# print("Number of vowels:", count)
# op: Number of vowels:3

# Task 9 - Print numbers in reverse order from 10 to 1.
# for i in range(10 , 0 , -1):
#     print(i)
# op : 10 9 8 7 6 5 4 3 2 1

# Task 10 - Print square of number from 1 to 5.
for i in range(1 , 6):
    print(i ** 2)
# op : 1 4 9 16 25