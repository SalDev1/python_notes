import pandas as pd

# DataFrame :- Dict-like Container
# Main tool for data analyst
fruits_sales = pd.DataFrame({"Apples": [131, 71], "Bananas": [34, 45]}, index=[
                            '2017 Sales', '2018 Sales'])

print(fruits_sales)
"""We are using the pd.DataFrame() constructor to generate these DataFrame objects. 
The syntax for declaring a new one is a dictionary whose keys are the column names 
(Bob and Sue in this example), and whose values are a list of entries."""


# Creating a data = DataFrame and Series


# If DataFrame is the list then Series is the column/
# sERIES == A single column of Dataframe
numbers = pd.Series([1, 2, 3, 4, 5])
print(numbers)

# Perfect example of pd.Series
ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=[
                        'Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)

# Most we are working with the already created data.

# CSV.file = Comma-Separated Values
