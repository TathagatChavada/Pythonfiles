# Defining Function
# 1
def greet(name):
    print("Hello, " + name + " Good morning!")


greet('Tathagat')

print("\n")


# 2
def add_numbers(x, y):
    return x + y


print(add_numbers(68, 64))

print("\n")


# 3  To find the average of marks and its grade.
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    Total_Subjects = len(marks)
    average_marks = sum_of_marks / Total_Subjects
    return average_marks


def compute_grade(average_marks):
    if average_marks >= 80:
        grade = "A"
    elif average_marks >= 60:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "D"

    return grade


marks = [70, 88, 55, 90, 44]
A = find_average_marks(marks)
print("Your average marks is:", A)

B = compute_grade(A)
print("Your grade is:", B)

print("\n")


# 4
def Greet(name, msg):
    print("Hello", name)
    print(msg)


Greet("Jack", "What's is going on")

print("\n")

# Code to find the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = 3
print("The factorial of num is:", n, "is", factorial(n))

# OR YOU CAN WRITE THIS

""" n=int(input("Input a number to compute the factiorial : "))
print(factorial(n)) """

print("\n")

#Global Variables
x = "global"

def foo():
    print("x inside:", x)

foo()
print("x outside:", x)

print("\n")

#Local Variable
def multiplication():
    x = "Hello World"
    print(x)
    for y in x:
        print(y)

multiplication()