import random

name = input("Who are you?\n")
print(f"Hello, {name}!")

print("Tossing a coin...")

heads = 0
tails = 0

for i in range(1, 4):
    if random.randint(0,1) == 1:
        print(f"Round {i}: Heads")
        heads += 1
    else:
        print(f"Round {i}: Tails")
        tails += 1

print(f"Heads: {heads}, Tails: {tails}")