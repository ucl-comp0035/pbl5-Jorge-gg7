import pandas as pd


def set_pandas_display_options(df):
    """ Sets the pandas display options based on the shape of the dataframe

    :param DataFrame df: the data
    """
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_prepared.csv', parse_dates=['Start', 'End'], dtype={'Year': str})
    set_pandas_display_options(df)
    # Add code here to print the stats returned by describe
