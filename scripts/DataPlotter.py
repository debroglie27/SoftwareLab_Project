import pandas as pd
import matplotlib.pyplot as plt
from scripts.Globals import CRICKET_FORMATS, PLAYER_TYPES, check_folder


def data_plotter(dd: int, mm: int, yyyy: int) -> None:
    """
    Generate plots based on cricket data for a specific date (dd-mm-yyyy).

    Parameters:
    - dd (int): Day of the date.
    - mm (int): Month of the date.
    - yyyy (int): Year of the date.

    This function generates two types of plots for each cricket format and player type:
    1. Number of players for each cricket team.
    2. Average rating of players for each cricket team.

    Additionally, it generates these plots for an "overall" category (without specifying player type) for each cricket format.

    The generated plots are saved in the 'plots' directory in PNG format.

    Example usage:
    data_plotter(1, 1, 2023)  # Generates plots for January 1, 2023 cricket data.
    """

    print("Generating Plots...")

    # Checking whether 'plots' folder exists, if not then create 'plots' folder
    check_folder('plots')

    for cricket_format in CRICKET_FORMATS:
        for player_type in PLAYER_TYPES:
            # Reading the csv file
            df = pd.read_csv(f'./csv/{cricket_format}_{player_type}_{dd}-{mm}-{yyyy}.csv')

            # Declaring 2 figures
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

        # Declaring 2 figures
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
