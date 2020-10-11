#1 Tuples:- A datatype for immutable ordered sequences of elements.

Location = (13.54323, 64.436213)
print("Enemy's ship is at latitude:",Location[0])
print("Enemy's ship is at longitude:",Location[1])
print("\n")

Dimensions = 50, 35, 20
l, b, h =  Dimensions

print("The dimensions are {}*{}*{}".format(l, b, h))


#2
from collections import namedtuple

a = namedtuple('Courses', 'Application, Technology')
s = a('Open CV', 'Detection and Recognition')

print(s)
