Countries = ["India", "Japan", "USA", "Brazil"]

for Country in Countries:
    print(Country.title())

print("\n")

# range(Start,Stop,Step)
print(list(range(5)))

print(list(range(1, 15, 2)))

for numbers in range(5):
    print(numbers)

for I in range(4):
    print("Hello")

print("\n")
#3
Weapons = ["katana", "sai", "kasurigama", "whip katars"]

for index in range(len(Weapons)):
   Weapons[index] = Weapons[index].title()
   print(Weapons)