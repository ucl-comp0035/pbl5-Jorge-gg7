# Pandas cheat sheet

| Purpose | Code |
| :----- | :----- |
| Use pandas in a code file | `import pandas as pd` |
| Read CSV | `df = pd.read_csv('my_data_file.csv')`  |
| Write to CSV | `df.to_csv('my_new_data_file.csv')` |
| Read Excel | `df = pd.read_excel('my_data_file.xlsx', 'sheet1')`  |
| Write to Excel | `df.to_excel('my_new_data_file', sheet_name='sheet1')` |
| Skip n rows on read | `df = pd.read_csv('my_data_file.csv', skiprows=1)` | 
| Number of rows/cols | `df.shape` |
| Top n rows | `df.head(5)` |
| Column labels | `df.columns` |
| Column labels and data types| `df.info(verbose=True)` |
| Drop a named column | `df.drop(['Source for Re-opening'], axis=1)` |
| Drop numbered columns | `df.drop(df.columns[[40, 41]], axis=1)` |
| Find missing values | `df.isnull()` and `df.isna()` |
| Count missing values in each row | `df.isnull().sum()` and `df.isna().sum()`|
| Count total missing values in the dataframe | `df.isnull().sum().sum()` and `df.isna().sum().sum()` |
| Create a new dataframe with the rows with missing values | `df_isna = df[df.isna().any(axis=1)]` |
| Drop null values | `df.dropna()` |
| Replace missing values with `fillna` | `df.fillna({'Column A': 0, 'Column B': 99, 'Column C': df['Column C'].mean()})`, `df.fillna(method='ffill', axis=1)`, `df.fillna(value=5)`  |
| Replace missing values with a particular value e.g. mean | `mean = df['col1'].mean()` then `df['col1'].fillna(mean)` |
| Filter rows | Rows where the value in col1 is greater than 10`df[df['col1']>10]` |
| Modify and replace the contents of the dataframe | Use `inplace=True` e.g. df =   |
| Find unique values | `df['col1'].unique()` |
| Number of occurrences of a value | `df['col1'].value_counts()` |
| Identify duplicates | `df.duplicated()` |
| Drop duplicates | `df.drop_duplicates(inplace=True)`, `df.drop_duplicates(subset=['col2'], inplace=True)`, `df.drop_duplicates(subset=['col2'], keep='last', inplace=True)` |
| Remove blank spaces | `df['col1'].str.strip()` |
| Merge multiple data frames | `pd.merge(df1, df2, on='name_of_common_column', how='outer'` (options for `how=` include left, right and inner)` |
| Concatenate multiple data frames | `pd.concat([df1, df2])` |
| (Not in how to's but likely useful) Splitting data into groups; applying functions to groups; and combining results into a data structure | `df.groupby('column1').sum()`, `df2 = df.groupby(['col1','col2']).count()` |
| Convert string to date | `df['ColumnName'] = pd.to_datetime(df['ColumnName'], format='%d%m%Y'` specify your [date format](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) |
| Boxplot with each variable in a subplot | `import matplotlib.pyplot as plt` `bp = df.plot.box(subplots=True)` `plt.show()` |
| Save plot (example using boxplot) | `df.boxplot(column=['Duration']).get_figure().savefig('images/bp_duration.png')` |