import pandas as pd


def prepare_data(df):
    """
    Prepares the paralympics data using the steps covered in PBL4
    and saves as a .csv

    :param DataFrame df: the raw data
    """
    df.drop(['Events', 'Sports', 'Countries'], axis=1, inplace=True)
    df.dropna(axis=0, subset=['Participants (M)', 'Participants (F)'], inplace=True)
    df.fillna({'Type': 'Winter'}, inplace=True)
    df['Type'] = df['Type'].str.strip()
    df_noc = pd.read_csv('data/noc_regions.csv')
    df_noc.drop(['notes'], axis=1, inplace=True)
    df = df.merge(df_noc, how='left', left_on='Country', right_on='region')
    df.drop(['region'], axis=1, inplace=True)
    df['NOC'].mask(df['Country'] == 'Great Britain', 'GBR', inplace=True)
    df['NOC'].mask(df['Country'] == 'Republic of Korea', 'KOR', inplace=True)
    df["Start"] = df["Start"] + '-' + df["Year"].astype(str)
    df["End"] = df["End"] + '-' + df["Year"].astype(str)
    df['Start'] = pd.to_datetime(df['Start'], format='%d-%b-%Y')
    df['End'] = pd.to_datetime(df['End'])
    df['Duration'] = df['End'] - df['Start']
    df['Duration'] = df['Duration'].dt.days.astype('int')
    df.to_csv('data/paralympics_prepared.csv', index=False)


if __name__ == '__main__':
    df_raw = pd.read_csv('data/paralympics_raw.csv')
    prepare_data(df_raw)
