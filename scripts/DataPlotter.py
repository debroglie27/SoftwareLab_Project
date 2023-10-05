import os
import pandas as pd
import matplotlib.pyplot as plt
from scripts.config import cricket_formats, player_types


def data_plotter(day, month, year):
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(project_directory, 'plots')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

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
            plt.savefig(f'./plots/{cricket_format}_{player_type}-1.png')

            # Plot 2
            mean_score = df.groupby('Team')['Rating'].mean()
            plt.figure(figsize=(10, 5))
            plt.title('Average Rating of Players for each Cricket Team')
            plt.xlabel('Cricket Teams')
            plt.ylabel('Average Rating')
            plt.bar(mean_score.index, mean_score.values)
            plt.savefig(f'./plots/{cricket_format}_{player_type}-2.png')
