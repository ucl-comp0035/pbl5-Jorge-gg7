import pandas as pd


def set_pandas_display_options(df):
    """ Sets the pandas display options based on the shape of the dataframe

    :param DataFrame df: the data
    """
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


def prepare_data(df):
    """
    Prepares the paralympics data using the steps covered in PBL4

    :param DataFrame df: the raw data
    :return: the prepared paralympic data
    :rtype: DataFrame
    """
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)
    df['Type'] = df['Type'].str.strip()
    df_noc = pd.read_csv('data/noc_regions.csv')
    df_noc.drop(['notes'], axis=1, inplace=True)
    df_merged = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df_merged.drop(['region'], axis=1, inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR', inplace=True)
    df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR', inplace=True)
    return df_merged


if __name__ == '__main__':
    df_raw = pd.read_csv('data/paralympics_raw.csv')
    df_prepared = prepare_data(df_raw)
    set_pandas_display_options(df_prepared)

    # A possible solution to the challenge, please share if you have a neater or more efficient solution!

    # Check the data type of the columns
    # print(df_prepared[['Year', 'Start', 'End']].dtypes)

    # Check the format of the strings in Start and End by printing a couple of rows
    # print(df_prepared[['Year', 'Start', 'End']].head(2))

    # Add the year to the Start and End columns. Year is int and Start/End are strings so to combine as strings you
    # need to first convert the Year to string
    # TODO: Consider if there is a case where the dates span year end e.g. December to January)
    df_prepared["Start"] = df_prepared["Start"] + '-' + df_prepared["Year"].astype(str)
    df_prepared["End"] = df_prepared["End"] + '-' + df_prepared["Year"].astype(str)
    print(df_prepared[['Year', 'Start', 'End']].head(2))
    print(df_prepared[['Year', 'Start', 'End']].dtypes)

    # Change the column datatype to date-time format
    # Pandas to_datetime  handles most date formats so you can run the following without the format= and it will work
    # date time formats are here for reference https://docs.python.org/3/library/datetime.html
    df_prepared['Start'] = pd.to_datetime(df_prepared['Start'], format='%d-%b-%Y')
    df_prepared['End'] = pd.to_datetime(df_prepared['End'])
    print(df_prepared[['Year', 'Start', 'End']].head(2))
    print(df_prepared[['Year', 'Start', 'End']].dtypes)

    # Create a duration column that calculates days between the start and end
    df_prepared['Duration'] = df_prepared['End'] - df_prepared['Start']
    print(df_prepared.head(5))

    # The output of the above is in timedelta format, however we want to compare duration as int
    # Convert the format
    print(df_prepared['Duration'].dtypes)
    df_prepared['Duration'] = df_prepared['Duration'].dt.days.astype('int')
    print(df_prepared['Duration'].dtypes)

    # Save the prepared data to CSV
    df_prepared.to_csv('data/data_prepared.csv')
