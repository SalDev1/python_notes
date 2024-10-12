import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# Data type of column in DataFrame or Series is known as dtype
# dtype = helps us to find what kind of data type is using for that particular column.
print(reviews.points.dtype)
print(reviews.dtypes)

# To check for NaN values in the selected column
reviews[pd.isnull(reviews.country)]

# This helps us to fill the missing values of column region_2
reviews.region_2.fillna("Unknown")

# If the person changes it's username
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

"""It's possible to convert a column of one type into another 
wherever such a conversion makes sense by using the astype() function."""
reviews.points.astype('float64')
