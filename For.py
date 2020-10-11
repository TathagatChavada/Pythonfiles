# 1
Fruits = ['Mango', 'Apple', 'Grapes']

for fruit in Fruits:
    print('Available fruit: ', fruit)

print('Good Bye!')

print('\n')

# 2

Num = int(input("Enter the number: "))
Factorial = 1

if Num < 0:
    print("Must be positive.")
elif Num == 0:
    print("Factorial = 1")
else:
    for i in range(1,Num + 1):
        Factorial = Factorial * i

print(Factorial)