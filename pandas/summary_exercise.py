import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)


def stars(reviews):
    if(reviews.points >= 95):
        return 3
    elif(reviews.country == "Canada"):
        return 3
    elif(reviews.points >= 85):
        return 2
    else:
        return 1


star_ratings = reviews.apply(stars, axis="columns")
