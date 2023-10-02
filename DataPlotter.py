import pandas as pd
import matplotlib.pyplot as plt
from config import cricket_formats, player_types


def data_plotter(day, month, year):
    for cricket_format in cricket_formats:
        for player_type in player_types:
            df = pd.read_csv(f'./csv/{cricket_format}_{player_type}_{day}-{month}-{year}.csv')
            print(df.head())

            # generate a frequency count of each category
            counts = df['Team'].value_counts()

            # create a bar plot
            plt.figure(figsize=(10, 5))
            plt.bar(counts.index, counts.values)
            plt.show()

            mean_score = df.groupby('Team')['Rating'].mean()
            plt.figure(figsize=(10, 5))
            plt.bar(mean_score.index, mean_score.values)
            plt.show()
