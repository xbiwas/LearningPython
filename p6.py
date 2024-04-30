import pandas as pd

readData = pd.read_csv("Book1.csv")
print(readData)
print(readData.head(5))
print(readData.dtypes)