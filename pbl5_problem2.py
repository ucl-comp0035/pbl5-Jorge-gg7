import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_prepared.csv', parse_dates=['Start', 'End'], dtype={'Year': str})
    # Add code here to create the box plot
    bp = df.plot.box()
    bp_sub = df.plot.box(subplots=True)
    plt.show()