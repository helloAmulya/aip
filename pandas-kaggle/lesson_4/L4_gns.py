# Grouping and Sorting

import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

print(reviews.groupby("points").points.count())
# print(reviews.points.value_counts()) >>> value_counts() is just a shortcut to groupby()


print(
    reviews.groupby("points").price.min()
)  # group the points and get the minimum price from that grouped points col
"""
now these specific operations cannot be done using value_counts()
what to use when? >>> if just counting occurence, use : value_counts
if need to group by one column and calculate something on a different column : groupby(), then the operation on that
"""

print(
    reviews.groupby("country").points.min()
)  # get the minimum points for that country


# print(reviews.groupby("winery").apply(lambda df: df.title.iloc[0]))  # imp, just to know
print(reviews.groupby("winery")["title"].first())  # this is more faster and optimised


print("—————————————————————————————————————————————")

print(
    reviews.groupby(["country", "province"]).apply(
        lambda df: df.loc[df.points.idxmax()]
    )
)

print(
    reviews.groupby(["country"]).price.agg([len, min, max])
)  # get the max, min price of the wine in the country

reviews.groupby(["points"]).price.agg([len, max, min])
"""
here it means group the data acc to points considering their price and give the len, max and min from them
"""
