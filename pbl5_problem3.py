import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    cols = ["Participants (M)", "Participants (F)", "Participants"]
    df = pd.read_csv('data/paralympics_prepared.csv', usecols=cols)
    df.rename(columns={"Participants (M)": "Male", "Participants (F)": "Female", "Participants": "Total"}, inplace=True)
    # Add code here to create and show the line plot
    df.plot.line()
    plt.show()