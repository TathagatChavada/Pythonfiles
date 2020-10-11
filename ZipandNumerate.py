Items = ["GPU Driver", "Alienware Area 51m", "Headphones", "Smartphones"]
Weights = [2, 1, 1, 3]

print(list(zip(Items, Weights)))

print("\n")

for Items, Weights in zip(Items, Weights):
    print(Items, Weights)

print("\n")

Laptops = [("Alienware Area 51m", 1), ("Acer Predator Triton", 1), ("Lenovo Legion", 1), ("Asus ROG Zephyrus", 1)]

GL, Quantity = zip(*Laptops)
print(GL)
print(Quantity)

print("\n")

GPU = ["NVIDIA", "AMD", "Intel"]

for i, GPU in enumerate(GPU):
    print(i, GPU)