import numpy as np
from sklearn.linear_model import LinearRegression

years = np.array([2000, 2002, 2005, 2007, 2010]).reshape(-1, 1)
percentage = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

model = LinearRegression()

model.fit(years, percentage)

year = np.array([[2015]])
predicted_percentage = model.predict(year)

year2 = np.array([[2017]])
predicted_percentage2 = model.predict(year2)

year3 = np.array([[2023]])
predicted_percentage3 = model.predict(year3)

print(f"Przewidywany procent bezrobotnych dla roku 2015: {predicted_percentage[0]:.3f}%")
print(f"Przewidywany procent bezrobotnych dla roku 2017: {predicted_percentage2[0]:.3f}%")
print(f"Przewidywany procent bezrobotnych dla roku 2023: {predicted_percentage3[0]:.3f}%")
print(f"W roku 2023 procent bezrobotnych przekroczy 12 p.p.")