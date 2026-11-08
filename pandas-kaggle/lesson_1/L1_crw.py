# working with pandas, Kaggle Learn

import pandas as pd

# Dataframe is a constructor
print(pd.DataFrame({"Yes": [50, 21], "No": [131, 2]}))  # integer based

pd.DataFrame({"Bob": ["b.val1", "b.val2"], "Sue": ["s.val1", "s.val2"]})  # string based

ex_index = pd.DataFrame(
    {
        "Bob": ["b.val1", "b.val2"],
        "Sue": ["s.val1", "s.val2"],
    },  # always add the comma then use the index outside {}, will throw error
    index=[
        "prod_A",
        "prod_B",
    ],  # by default the indexes as 0 and 1, we can change them using 'index'
)
print(ex_index)

# if DataFrame is a table, then Series is a list >> imp

ex_series = pd.Series([1, 2, 3, 4, 5, 6])
print(ex_series)


series_and_datafr = pd.Series(
    [30, 32, 43],
    index=["2015 Sales", "2016 Sales", "2017 Sales"],
    name="Prod_A",  # here, Prod_A is the name of series
)
print(series_and_datafr)

# csv loaded into pandas, becomes a DataFrame
ex_read = pd.read_csv("./winemag-data-130k-v2.csv")  # reading a csv
print(ex_read.shape)  # check how large the DataFrame is

ex_withcol_read = pd.read_csv(
    "./winemag-data-130k-v2.csv", index_col=0
)  # this tells pandas to use the first col in the csv as the index instead of creating a new one
print(ex_withcol_read.shape)


# to save a DataFrame to disk as a csvFile

ex_withcol_read.to_csv("kaggle_tut1_example.csv")  # define the name you want
# ex_withcol_read.to_csv("kaggle_tut1_example.csv", index=False) use this if the dataframe already has a index
