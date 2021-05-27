import math

#x = [-b+sqrt(b^2 -4ac)]/2a...[-b-sqrt(b^2 -4ac)]/2a
"""This example solves quantratic equation
    Round of the answer to 4dp
"""

def quantratic():
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    squareRoot = math.sqrt(b*b - 4 * a * c)

    quantratic1 = (-b + squareRoot) / (2 * a)
    quantratic2 = (-b - squareRoot) / (2 * a)

    print("Answer is: ", round(quantratic1,4), "or", round(quantratic2,4))
    
quantratic()
    
