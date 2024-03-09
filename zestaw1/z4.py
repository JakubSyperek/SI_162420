import numpy as np

d = np.loadtxt("car.txt", dtype=str)

attribute = d[:, 1].astype(float)

average = np.mean(attribute)

procent = int(0.1 * len(attribute))
random_indices = np.random.choice(range(len(attribute)), procent, replace=False)

attribute[random_indices] = np.nan

attribute = np.where(np.isnan(attribute), average, attribute)

print("\n", attribute)
