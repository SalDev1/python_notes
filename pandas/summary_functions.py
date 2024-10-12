import pandas as pd

results = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(results)

'''This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes 
based on the data type of the input.'''
print(results.points.describe())

# Some Summary Functions
# It can help you summarize the data according to your desire output
print(results.points.mean())

print(results.taster_name.unique())

print(results.taster_name.value_counts())

results_points_mean = results.points.mean()
"""Map function helps you to map values to different set of values"""
print(results.points.map(lambda p: p-results_points_mean))

# Modifying each value of the column(points == previous point - mean value)
# apply() = helps in modifying some or all values of the selected column in dataset.


def remean_points(row):
    row.points = row.points - results_points_mean
    return row

# print(results.apply(remean_points, axis="columns"))
# print(results.points)


print(results.country + "-" + results.region_1)

# Creating a series of no of times "tropical" and "fruity" has been seen in each description
n_trop = results.description.map(lambda desc: 'tropical' in desc).sum()
n_fru = results.description.map(lambda desc: 'fruity' in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fru], index=['tropical', 'fruity'])
