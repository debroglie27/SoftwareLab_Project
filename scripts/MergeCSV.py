import os
import pandas as pd
from scripts.globals import cricket_formats, check_folder


def filter_files(filename, dd, mm, yyyy):
    # Extract the date from the filename
    date_parts = filename.split('_')[2].split('.')[0].split('-')
    DD, MM, YYYY = map(int, date_parts)

    return DD == dd and MM == mm and YYYY == yyyy


def merge_csv(dd, mm, yyyy):
    folder_path = check_folder('csv')

    all_filenames = os.listdir(folder_path)
    all_filenames = list(filter(lambda filename: filter_files(filename, dd, mm, yyyy), all_filenames))

    for cricket_format in cricket_formats:
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


if __name__ == "__main__":
    from scripts.globals import day, month, year
    merge_csv(day, month, year)
