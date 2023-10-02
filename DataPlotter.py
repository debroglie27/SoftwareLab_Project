import os
import pandas as pd
import matplotlib.pyplot as plt
from config import cricket_formats, player_types


def data_plotter(day, month, year):
    if not os.path.exists("./plots"):
        os.makedirs("./plots")

    for cricket_format in cricket_formats:
        for player_type in player_types:
            df = pd.read_csv(f'./csv/{cricket_format}_{player_type}_{day}-{month}-{year}.csv')

            # Plot 1
            counts = df['Team'].value_counts()
            plt.figure(figsize=(10, 5))
            plt.title('No. of Players for each Cricket Team')
            plt.xlabel('Cricket Teams')
            plt.ylabel('No. of Players')
            plt.bar(counts.index, counts.values)
            plt.savefig(f'./plots/{cricket_format}_{player_type}_{day}-{month}-{year}-1.png')

            # Plot 2
            mean_score = df.groupby('Team')['Rating'].mean()
            plt.figure(figsize=(10, 5))
            plt.title('Average Rating of Players for each Cricket Team')
            plt.xlabel('Cricket Teams')
            plt.ylabel('Average Rating')
            plt.bar(mean_score.index, mean_score.values)
            plt.savefig(f'./plots/{cricket_format}_{player_type}_{day}-{month}-{year}-2.png')
