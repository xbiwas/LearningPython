import pandas as pd
df = pd.DataFrame(
        {
            "Name": [
                "Asish",
                "Sajina",
                "Bot",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
print(df)
print(df["Age"])
print(df["Name"])
print(df["Sex"])
print(df["Age"].max())

print(df.describe())