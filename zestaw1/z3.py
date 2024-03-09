import pandas as pd

car = pd.read_csv('car.txt', sep=" ", header=None)
cartype = pd.read_csv('car-type.txt', sep=" ", header=None)

print("3a")
print(car.iloc[:, -1].unique())

print("3b")
print(car.iloc[:, -1].value_counts())

print("3c")
atrybuty = cartype[cartype[1] == 'n'][0]
for i in cartype:
    print("Min: ", i, car[i].min())
    print(" ")
    print("Max: ", i, car[i].max())

print("3d")
for i in car.columns:
    print(i, car[i].nunique())

print("3e")
for i in car.columns:
    print(i, car[i].unique())

dc = car.iloc[:,-1].unique()

print("3f")
for i in atrybuty:
    print(i, car[i].std())
    for j in dc:
        print(i, j, car[car.iloc[:, -1] == j][i].std())

