# multi indexes and orting

import pandas as pd

reviews = pd.read_csv("./winemag-data-130k-v2.csv", index_col=0)

countries_reviewed = reviews.groupby(["country", "province"]).description.agg([len])

print(countries_reviewed)

mi = countries_reviewed.index
print(type(mi))  # multi-index
print(countries_reviewed.index)


# clearn, flat DataFrame for further operations
summary = (
    reviews.groupby(["country", "province"])["price"]
    .agg(["count", "mean"])
    .reset_index()
)

# easy to filter or sort
summary[summary["count"] > 500].sort_values("mean", ascending=False)


countries_reviewed = countries_reviewed.reset_index()

print(
    countries_reviewed.sort_values(by="len")
)  # we can sort by more than one col >>> (by=['country', 'len'])
print(
    countries_reviewed.sort_values(by="len", ascending=False)
)  # now it will print in descending


print(countries_reviewed.sort_index())


# What are the most expensive wine varieties? Create a variable `sorted_varieties` containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties)
pex = reviews.groupby("variety").price.agg(["min", "max"])
sorted_varieties = pex.sort_values(
    by=["min", "max"], ascending=False
)  # we can pass both cols max and min in 'by'


reviews.groupby(["taster_name"]).points.mean().rename_axis(
    "reviewers"
)  # this will change the heading to "reviewers"

reviews.groupby(["country", "variety"]).size().sort_values(ascending=False)
