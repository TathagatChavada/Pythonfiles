Fullforms = {
    "AWM" : "Artic Warfare Magnum",
    "SSD" : "Solid State Drive",
    "HDD" : "Hard Disk Drive",
    "Hydrogen" : {"Atomic Number" : 1,
                  "Weight" : 1.00794,
                  "Symbol" : 'H'}
}
# Updating
Fullforms["fdhgrgh"]="Drive"
Fullforms["AWM"]= 111

print(Fullforms)

print('\n')
for x,y in Fullforms.items():
    print(x,y)

print(Fullforms.pop("AWM"))
del Fullforms["SSD"]
print(Fullforms)

print('\n')

print('\n')
# Chainmap

from collections import ChainMap

a = {1: 'Pyhton', 2: 'AI'}
b = {3: 'MI', 4: 'Open CV'}

c = ChainMap(a,b)

print(c)

print('\n')


# Counter
from collections import Counter

A = [1,1,2,3,2,3,3,4,5,4,4,5]
B = Counter(A)

print(B)
print(list(B.elements()))
print(B.most_common())

print('\n')
