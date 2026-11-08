import pandas as pd

reviews = pd.read_csv("kaggle_tut2_ex.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# print(reviews.shape)
# print(reviews.country) # access the country property
print(reviews["country"][1])  # get single specific value

print("————————————————————————————")
print("index based selection\n")
# index based selection
print(reviews.iloc[0])  # this will give the data in the very first row of DataFrame
print(reviews.iloc[:, 2])  # this gives the column data for the index
print(reviews.iloc[:3, 0])  # this gives the first 3 values in the column at index 0
print(reviews.iloc[4:7, 2])  # values within row 4-7 (7 is excluded) at col index 2
print(reviews.iloc[[0, 1, 2], 0])  # can pass as a list and get only those values

print("————————————————————————————")
print("label based selection\n")
# label based selection
print(reviews.loc[0, "country"])

"""
iloc excludes the last index i.e. [3:12] will have - 3,4,5....11
loc consists of the last index i.e. [3:12] will have - 3,4,5....12

also, iloc will search for the row and count it from 3 to 12
loc will look for the label (text) 3 and will consider it

use iloc
"""


# when to use the below? —> if dataset has meaningful indices
print(reviews.loc[:, ["taster_name", "taster_twitter_handle", "title"]])

print(reviews.loc[:5, ["taster_name", "taster_twitter_handle", "title"]])


print(
    reviews.loc[reviews.country == "Italy"]
)  # gives all the rows with country as Italy
print(
    reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)]
)  # gives wine from Italy with points more than equal to 90
print(
    reviews.loc[(reviews.country == "Italy") | (reviews.points >= 90)]
)  # wine which is either from Italy or is rated above 90

reviews.loc[
    reviews.country.isin(["Italy", "France"])
]  # built-in pandas 'isin' conditional selector


reviews.loc[reviews.price.notnull()]
reviews.loc[reviews.price.isnull()]


reviews.info()
"""
<class 'pandas.DataFrame'>
RangeIndex: 129971 entries, 0 to 129970
Data columns (total 14 columns):
 #   Column                 Non-Null Count   Dtype
---  ------                 --------------   -----
 0   country                129908 non-null  str
 1   description            129971 non-null  str
 2   designation            92506 non-null   str
 3   points                 129971 non-null  int64
 4   price                  120975 non-null  float64
 5   province               129908 non-null  str
 6   region_1               108724 non-null  str
 7   region_2               50511 non-null   str
 8   taster_name            103727 non-null  str
 9   taster_twitter_handle  98758 non-null   str
 10  title                  129971 non-null  str
 11  variety                129970 non-null  str
 12  winery                 129971 non-null  str
 13  critic                 129971 non-null  str
dtypes: float64(1), int64(1), str(12)
memory usage: 13.9 MB
"""


"""
reviews.head() → Displays the first 5 rows.
reviews.shape → Returns rows and columns.
reviews.columns → Returns column names.
reviews.dtypes → Returns data types.
reviews.info() → Gives an overall structural summary.
reviews.describe() → Gives statistical summaries of numerical columns.
"""


reviews["index_backwards"] = range(
    len(reviews), 0, -1
)  # adds new col and with reversed indexes
type(reviews["index_backwards"])  # <class 'pandas.Series'>


# chaining iloc and loc together

df = reviews.loc[:, ["country", "variety"]].iloc[
    :100
]  # this will get a DataFrame containing the country and variety columns for the first 100 rows


# a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand
top_oceania_wines = reviews.loc[
    (reviews.country.isin(["Australia", "New Zealand"])) & (reviews.points >= 95)
]
