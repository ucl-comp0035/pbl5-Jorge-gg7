import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('data/paralympics_prepared.csv', parse_dates=['Start', 'End'], dtype={'Year': str})
    # Add code here to create the box plot