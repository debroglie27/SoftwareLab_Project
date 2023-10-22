import pandas as pd
import matplotlib.pyplot as plt
from scripts.Globals import CRICKET_FORMATS, PLAYER_TYPES, check_folder


def data_plotter(dd, mm, yyyy):
    print("Generating Plots...")

    check_folder('plots')

    for cricket_format in CRICKET_FORMATS:
        for player_type in PLAYER_TYPES:
            # Reading the csv file
            df = pd.read_csv(f'./csv/{cricket_format}_{player_type}_{dd}-{mm}-{yyyy}.csv')

            plt.figure(0, figsize=(10, 5))
            plt.figure(1, figsize=(10, 5))

            # Plot 1 - No. of Players for each Cricket Team
            counts = df['Team'].value_counts()
            plt.figure(0)
            plt.title('No. of Players for each Cricket Team')
            plt.xlabel('Cricket Teams')
            plt.ylabel('No. of Players')
            plt.bar(counts.index, counts.values)
            plt.savefig(f'./plots/{cricket_format}_{player_type}-1.png')
            plt.close(0)

            # Plot 2 - Average Rating of Players for each Cricket Team
            mean_score = df.groupby('Team')['Rating'].mean()
            plt.figure(1)
            plt.title('Average Rating of Players for each Cricket Team')
            plt.xlabel('Cricket Teams')
            plt.ylabel('Average Rating')
            plt.bar(mean_score.index, mean_score.values)
            plt.savefig(f'./plots/{cricket_format}_{player_type}-2.png')
            plt.close(1)

        plt.figure(0, figsize=(10, 5))
        plt.figure(1, figsize=(10, 5))

        # Reading the csv file (Overall)
        df = pd.read_csv(f'./csv/overall_{cricket_format}_{dd}-{mm}-{yyyy}.csv')

        # Plot 1 - No. of Players for each Cricket Team (Overall)
        counts = df['Team'].value_counts()
        plt.figure(0)
        plt.title('No. of Players for each Cricket Team')
        plt.xlabel('Cricket Teams')
        plt.ylabel('No. of Players')
        plt.bar(counts.index, counts.values)
        plt.savefig(f'./plots/overall_{cricket_format}-1.png')
        plt.close(0)

        # Plot 2 - Average Rating of Players for each Cricket Team (Overall)
        mean_score = df.groupby('Team')['Rating'].mean()
        plt.figure(1)
        plt.title('Average Rating of Players for each Cricket Team')
        plt.xlabel('Cricket Teams')
        plt.ylabel('Average Rating')
        plt.bar(mean_score.index, mean_score.values)
        plt.savefig(f'./plots/overall_{cricket_format}-2.png')
        plt.close(1)

    print("Done")


if __name__ == "__main__":
    from scripts.Globals import current_date

    day, month, year = current_date()
    data_plotter(day, month, year)
