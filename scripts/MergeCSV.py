import os
import pandas as pd
from scripts.Globals import CRICKET_FORMATS, check_folder


def filter_files(filename, dd, mm, yyyy):
    """
    Check if a filename contains a date matching the specified day, month, and year.

    Parameters:
    - filename (str): The name of the file to be checked.
    - dd (int): The day to be matched.
    - mm (int): The month to be matched.
    - yyyy (int): The year to be matched.

    Returns:
    - bool: True if the date in the filename matches the specified day, month, and year; otherwise, False.

    This function is used to filter and identify files in a directory based on their filenames containing date information.
    It extracts the date parts from the filename, compares them to the specified date, and returns True if there is a match.

    Example usage:
    filter_files('odi_all-rounder_1-1-2023_data.csv', 1, 1, 2023)  # Returns True for matching date.
    filter_files('overall_t20i_15-2-2023_data.csv', 1, 1, 2023)  # Returns False for non-matching date.
    filter_files('test_bowling_2-7-2022_data.csv', 1, 1, 2023)  # Returns False for a filename without a date.
    """

    # Extract the date from the filename
    date_parts = filename.split('_')[2].split('.')[0].split('-')
    DD, MM, YYYY = map(int, date_parts)

    return DD == dd and MM == mm and YYYY == yyyy


def merge_csv(dd: int, mm: int, yyyy: int) -> None:
    """
    Merge CSV files containing cricket data for various formats and create an 'overall' CSV file.

    Parameters:
    - dd (int): Day of the date.
    - mm (int): Month of the date.
    - yyyy (int): Year of the date.

    This function merges CSV files for each cricket format, excluding files with names not matching the specified date.
    It creates an 'overall' CSV file for each cricket format by concatenating data from multiple player type CSV files.

    Example usage:
    merge_csv(1, 1, 2023)  # Merges CSV files for January 1, 2023, and creates 'overall' CSV files.
    """

    print("-"*40 + "\nMerging CSV Files...")

    # Checking whether 'csv' folder exists, if not then create 'csv' folder and returns folder path
    folder_path = check_folder('csv')

    # List of filenames inside the 'csv' folder
    all_filenames = os.listdir(folder_path)
    # Filtering filenames based on <dd, mm, yyyy>
    all_filenames = list(filter(lambda filename: filter_files(filename, dd, mm, yyyy), all_filenames))

    for cricket_format in CRICKET_FORMATS:
        # Filter out csv files with name starting with <cricket-format>
        csv_files = [f for f in all_filenames if f.startswith(f'{cricket_format}')]

        # Create a list to hold the dataframes
        df_list = []

        for csv_file in csv_files:
            file_path = os.path.join(folder_path, csv_file)

            # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)

        # Concatenate all data into one DataFrame
        merge_df = pd.concat(df_list, ignore_index=True)

        # Save the final result to a new CSV file
        merge_df.to_csv(os.path.join(folder_path, f'overall_{cricket_format}_{dd}-{mm}-{yyyy}.csv'), index=False)

    print("Done")


if __name__ == "__main__":
    from scripts.Globals import current_date

    day, month, year = current_date()
    merge_csv(day, month, year)
