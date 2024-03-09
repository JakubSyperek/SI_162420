import pandas as pd


df = pd.read_csv('Churn_Modelling.csv')
print(df.head())

df = pd.get_dummies(df, columns=['Geography'], drop_first=True)

print("\n")
print(df.head())

