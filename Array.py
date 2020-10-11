import array as arr

A = arr.array('i',[1,2,3,4,5])
print(A)

print(A[-2])

print(len(A))

# Adding an elements to an array
A.append(6)
print(A)

A.extend([78,88,98,108])
print(A)

# Removing elements from an array
print(A.pop())
A.remove(1)
print(A)


print("\n")

Games = ["Apex Legends", "Call of Duty", "God of War", "Resident Evil"]
print(Games)

for x in Games:
    print(x)

print("\n")

print(Games[0:3])

print("\n")

for x in Games[0:2]:
    print(x)

print("\n")

B = 0

while B < len(Games):
    print(Games[B])
    B += 1


