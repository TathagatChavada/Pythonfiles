# 1 Calculating the volume of cylinder
def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 5))

print("\n")

# 2
egg_count = 0

def buy_eggs(count):
    return count + 12  # purchase a dozen eggs

egg_count = buy_eggs(egg_count)
print(buy_eggs(10))

print("\n")

#3
