'''
1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
 also create a lambda function that multiplies argument x with argument y and print the result.
Example of a lambda function:
x = lambda a : a + 10
print(x(5))
Would return 15
'''

addFifteen = lambda x: x + 15

xTimesY = lambda x, y: print(x * y)

xTimesY(5, 6)