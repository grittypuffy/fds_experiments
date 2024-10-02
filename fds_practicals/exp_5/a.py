"""
Write a Pandas Dataframes to create a dataframe using a list of Elements.
"""
import pandas as pd

def pandas_dataframe():

    data = [
        ['London', 'UK', 8908081],
        ['New York', 'USA', 8419600],
        ['Tokyo', 'Japan', 13929286],
        ['Sydney', 'Australia', 5312163],
        ['Cairo', 'Egypt', 9915278]
    ]

    df = pd.DataFrame(data, columns=['City', 'Country', 'Population'])
    print(df)