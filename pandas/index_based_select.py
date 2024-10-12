import pandas as pd

# Index Operator = []
amazon_data = pd.read_csv('1429_1.csv', index_col=0)

print(amazon_data['name'][0])

"""Index-based selection¶
Pandas indexing works in one of two paradigms. The first is index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
To select the first row of data in a DataFrame, we may use the following:"""

print(amazon_data.iloc[0])

# Normal Python == row first , column second
# Native Python == column first , row second
print(amazon_data.iloc[:, 0])

# Showing the ids of the first ,second and third row.
# iloc[:number of rows that we want to show , selecting columns]
print(amazon_data.iloc[:4, 2])

# Showing you the last three rows in the csv file with column 0
print(amazon_data.iloc[:-3, 0])
