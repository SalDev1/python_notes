import pandas as pd

# Index Operator = []
amazon_data = pd.read_csv('1429_1.csv', index_col=0)

# loc[] = Labeled-Based-Selection , it mainly focuses on the columns given in the csv file
print(amazon_data.loc[:, ['name', 'asins', 'brand', 'categories']])

"""iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10."""
print(amazon_data.iloc[:100, [0, 1]])  # Index-Based
# OR
print(amazon_data.loc[:99, ['name', 'brand']])  # Label-Based

print(amazon_data.loc[amazon_data.brand == "Amazon"])

# You can conditions as well to get the desired data you are looking for.
# top_oceania_wines = reviews[(reviews.points >= 95) & (
#     (reviews.country == "Australia") | (reviews.country == "New Zealand"))]
# top_oceania_wines
