import pandas as pd

pd.set_option('max_rows', 5)
results = pd.read_csv('winemag-data-130k-v2.csv', index_col=5)

# rename() == let's you change index name or column name
modified_results = results.rename(columns={'points': 'score'})
# Your chnages has sucessfully being modified.
print(modified_results.score)

# Modifying the names of some rows
modified_results_1 = results.rename(index={0: 'firstEntry', 1: "secondEntry"})
print(modified_results_1)

# Rename_axis == helps you to rename x-axis and y-axis
modified_results_2 = results.rename_axis(
    "wines", axis="rows").rename_axis("fields", axis="columns")
print(modified_results_2)
