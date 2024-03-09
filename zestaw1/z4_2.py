import numpy as np

d = np.loadtxt("car.txt", dtype=str)

attribute = np.loadtxt("car.txt", dtype=str, usecols=1)
average = np.mean(attribute)

procent = int(0.1*len(d))
random_indices = np.random.choice(range(len(attribute)), procent, replace=False)

attribute = np.asarray(attribute, dtype=str)
for random_indices in random_indices:
    attribute[random_indices] = "?"

print("\n", attribute)

for x in range(len(attribute)):
    if attribute[x] == "?":
        attribute[x] = average

attribute = np.asarray(attribute, dtype=float)
print("\n", attribute)