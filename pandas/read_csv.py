import pandas as pd


animals = pd.DataFrame({"Cows": [12, 20], "Goats": [22, 19]}, index=[
                       'Year 1', 'Year 2'])
# print(animals)

# animals.to_csv("cows_and_goats.csv")

# print(pd.read_csv("cows_and_goats.csv", index_col=0))
# help(pd.read_csv)


amazon_data = pd.read_csv('1429_1.csv', index_col=0)

print(amazon_data['name'][0])
