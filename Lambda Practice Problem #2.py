'''
3. Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

b = sorted(a, key = lambda x: x[1])
print(b)

#key refers to which element of the tuple you want to sort, in this example we put x[1] as the key to organize the tuple by the scores.