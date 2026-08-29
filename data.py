import pandas as pd

data = {
    "name": ["Loki", "Sara", "John"],
    "age": [25, 30, 22],
    "city": ["Tetovo", "Skopje", "Ohrid"]
}

df = pd.DataFrame(data)
print(df)
print(df[df["age"] > 24])
print(df["name"])
print(df["age"].mean())
