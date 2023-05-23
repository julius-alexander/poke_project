import random

random.seed(42)

for i in range(6):
    for j in range(6):
        print(random.randint(0, 31))
    print()
