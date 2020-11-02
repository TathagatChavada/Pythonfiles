# Triangle
for i in range(4):
    for j in range(i+1):
        print("* ",end="")

    print()


print("\n")

# Inverted Triangle
for i in range(4):
    for j in range(4-i):
        print("* ", end="")

    print()

# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(i):
            # printing stars                                   # eval
            print("* ", end="")

            # ending line after each row
        print("")

    # Driver Code
n = 5
pypart(n)


# Pyramid
def pattern(m):
    k = m * 2
    for i in range(0,m):
        for j in range(0,k):
            print(end=" ")
        k = k - 2
        for j in range(0,i+1):
            print("*", end=" ")
        print("\r")
pattern(3)


