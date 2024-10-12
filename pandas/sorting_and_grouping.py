import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)


"""Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column. 
However, often we want to group our data, and then do something specific to the group the data is in."""

groupby_function = reviews.groupby('points').points.count()
"""groupby() created a group of reviews which allotted the same point values to the given wines. 
Then, for each of these groups, we grabbed the points() column 
and counted how many times it appeared. value_counts() is just a shortcut to this groupby() operation."""

# print(groupby_function)

# # Selecting the name of the first wine reviewed from each winery in the dataset
# print(reviews.groupby('winery').apply(lambda p: p.title.iloc[0]))

# # Selecting the best wine by country and province
# print(reviews.groupby(['country', 'province']).apply(
#     lambda p: p.loc[p.points.idxmax()]))

# # Agg function = allows you to run multiple functions at the same time
# print(reviews.groupby(['country']).agg([len, max, min]))

# Multi Indexing
# They also require two-levels of labels to retrieve a value
countries_reviewed = reviews.groupby(
    ['country', 'province']).description.agg([len])
print(countries_reviewed)

# Mostly common used func
print(countries_reviewed.reset_index())

# Result of the groupby , order of the rows depend upon the values in the index , not in the data.
countries = countries_reviewed.reset_index()
print(countries.sort.values(by="len"))

# Sort the data according to the value in the index.
print(countries.sort_index())

countries_reviewed.sort_values(by=['country', 'len'])
