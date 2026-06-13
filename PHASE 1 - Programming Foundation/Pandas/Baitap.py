import pandas as pd

data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, None, 45, 22],
    'Purchases': [3, 2, 5, 1, 4],
    'VIP': [False, True, False, True, False]
}
df = pd.DataFrame(data)
so_nan = df.isna().sum()
print(so_nan)
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)
target_customers = df[df['Purchases'] > 2]
print(target_customers)