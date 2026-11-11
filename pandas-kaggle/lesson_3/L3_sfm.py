# Summary Functions and Maps


import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)
# print(reviews.shape)
# print(reviews.iloc[:0])  # this will get you all the col names


# we us the summary functions to restructure the data into useful way

print(reviews.points.describe())
print(reviews.points.mean())
# print(reviews.variety.describe()) # use for numerrical data only, string ones make no sense
print(reviews.taster_name.unique())
print(reviews.points.value_counts())
print(reviews.variety.value_counts())


"""
describe() >>> restructure the data, useful for numerical data only
mean() >>> get mean of the numerical data
unique() >>> get the unique values
value_counts() >>> get the occurrences
"""


# map -> takes one set of values and "maps" them to another set of values
reviews_points_mean = reviews.points.mean()
reviews.points.map(
    lambda p: p - reviews_points_mean
)  # do not put reviews.points.mean() here, it will make it slow and recalculates average again and again

"""
lambda is used to define temporary one-line function in python
map() -> for a single colum (series)
apply() -> complete DataFrame
"""


# reviews.apply(lambda p: p - reviews_points_mean, axis="columns")


def remean_points(row, mean_val):
    row.points = row.points - mean_val
    return row


reviews.apply(remean_points, axis="columns", args=(reviews_points_mean,))


print(reviews.head(1))

# review_points_mean = reviews.points.mean()
# reviews.points - review_points_mean


print(reviews.country + " - " + reviews.region_1)
