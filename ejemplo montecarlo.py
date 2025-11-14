import random

dentro = sum(1 for h in range(10000000) if (random.random()**2 + random.random()**2) <= 1)
print(4 * dentro / 10000000)
