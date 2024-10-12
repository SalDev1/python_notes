import pandas as pd

canadian_youtube = pd.read_csv('CAvideos.csv', index_col=0)
british_youtube = pd.read_csv('GBvideos.csv', index_col=0)
pd.set_option('max_rows', 5)

# print(canadian_youtube)
# print(british_youtube)

# For Combine operations ==  you have join() , merge() . concat()
# print(pd.concat([canadian_youtube, british_youtube]))

# join() == helps you combine different DataFrame objects which has a common index in common.
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

print(left.join(right, lsuffix='_CAN', rsuffix="_US"))
