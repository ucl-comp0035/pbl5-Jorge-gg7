import matplotlib.pyplot as plt
import pandas as pd


def line_chart_mf_ratio(df):
    """ Generates a line chart displaying the changing ratio of male:female participants. """
    df['M:F'] = df['Male'] / df['Female']
    df_summer = df.loc[df['Type'] == 'Summer']
    df_winter = df.loc[df['Type'] == 'Winter']
    ax = df_summer.plot.line(y='M:F', label="Summer")
    df_winter.plot.line(ax=ax, y='M:F', label="Winter")
    ax.legend(['Summer', 'Winter'])
    plt.xticks(df.index, df["Year"].values)
    plt.xticks(rotation=90)
    ax.get_figure().savefig('images/ratio_line.png')
    plt.show()


if __name__ == '__main__':
    cols = ['Year', 'Type', 'Participants (M)', 'Participants (F)', 'Participants']
    df = pd.read_csv('data/paralympics_prepared.csv', usecols=cols, dtype={'Year': str, 'Type': str})
    df.rename(columns={"Participants (M)": "Male", "Participants (F)": "Female", "Participants": "Total"}, inplace=True)
    # line_chart_mf_ratio(df) # Uncomment to see the line chart version

    # 1. Sort the values by Type and Year
    # The syntax is `df.sort_values(["ColName1", "ColName2"], ascending=(Fale, True), inplace=True)`
    df.sort_values(["Type", "Year"], ascending=(True,True), inplace=True)

    # 2. Add two new columns that each contain the result of calculating the % of male and female participants (e.g.
    # Male/Total)
    df['M%'] = df['Male'] / df['Total']
    df['F%'] = df['Female'] / df['Total']
    # 3. Create a new column that combines Type and Year to use as the x-axis
    df['Event'] = df['Type'] + df['Year']

    # 4. Create the stacked bar plot of the % for male and female
    # Syntax `df.plot.bar(x='ColName1', y=['ColName2', 'ColName3'], stacked=True)`
    df.plot.bar(x='Event', y=['M%', 'F%'], stacked=True, xlabel='Paralympics Event')

    # The next line just ensures the x-axis labels are fully visible, you may need to adjust the value of 'bottom='
    plt.gcf().subplots_adjust(bottom=0.3)
    plt.show()
