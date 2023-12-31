import requests
from requests.exceptions import ConnectionError, HTTPError, RequestException
import pandas as pd
from bs4 import BeautifulSoup
from scripts.Globals import CRICKET_FORMATS, PLAYER_TYPES, save_latex_variables, check_folder


def web_scrapper(dd: int, mm: int, yyyy: int) -> None:
    """
    Scrape cricket player rankings data from the ICC website and save it as CSV files.

    Parameters:
    - dd (int): Day of the date.
    - mm (int): Month of the date.
    - yyyy (int): Year of the date.

    This function scrapes data for various cricket formats and player types from the ICC website.
    It saves the data as CSV files with a filename based on the date and player type.

    Example usage:
    web_scrapper(1, 1, 2023)  # Scrapes data for January 1, 2023.
    """

    print("-"*40 + "\nFetching Online Data...")

    base_url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/'

    # Checking whether 'csv' folder exists, if not then create 'csv' folder
    check_folder('csv')

    for cricket_format in CRICKET_FORMATS:
        for player_type in PLAYER_TYPES:
            # Creating the request url
            url = base_url + cricket_format + '/' + player_type

            try:
                # Getting the requested url
                page = requests.get(url)
                # Raises HTTPError for bad responses
                page.raise_for_status()
            except ConnectionError as conn_error:
                print(f"Error connecting to the server: {conn_error}")
                return
            except HTTPError as http_error:
                print(f"HTTP Error: {http_error}")
                return
            except RequestException as req_error:
                print(f"Request Error: {req_error}")
                return

            # Getting the html of the page
            soup = BeautifulSoup(page.text, 'html.parser')

            # Finding the table in the html
            table = soup.find('table')
            table_titles = [title.text.strip() for title in table.find_all('th')]

            # Finding all the rows in the table
            all_rows = table.find_all('tr')
            row_1st = all_rows[1].find_all('td')

            # Position 1 Player Details
            pos1_player_name = row_1st[1].div.find_all('div')[1].a.div.text.strip()
            pos1_player_team = row_1st[2].div.text.strip()
            pos1_player_rating = row_1st[3].div.text.strip()
            pos1_player_best_rating = row_1st[4].div.span.text.split('v')[0].strip()

            # Storing Position 1 Player Details in a Dictionary
            pos1_player = {f'{cricket_format}-{player_type}-name': pos1_player_name,
                           f'{cricket_format}-{player_type}-team': pos1_player_team,
                           f'{cricket_format}-{player_type}-rating': pos1_player_rating,
                           f'{cricket_format}-{player_type}-best-rating': pos1_player_best_rating}

            # Save the Position 1 Player for latex to use
            save_latex_variables(pos1_player, mode="a")

            table_row_1st = ['1', pos1_player_name, pos1_player_team,
                             pos1_player_rating, pos1_player_best_rating]

            # Initialising the dataframe using table titles
            df = pd.DataFrame(columns=table_titles)

            # Adding the 1st row in the dataframe
            length = len(df)
            df.loc[length] = table_row_1st

            for index, row in enumerate(all_rows[2:]):
                data = row.find_all('td')
                table_row = [f'{index+2}', data[1].a.text.strip(),
                             data[2].find_all('span')[1].text.strip(), data[3].text.strip(),
                             data[4].text.split('v')[0].strip()]

                # Adding the rows in the dataframe
                length = len(df)
                df.loc[length] = table_row

            # Saving the dataframe into a csv file
            df.to_csv(f'./csv/{cricket_format}_{player_type}_{dd}-{mm}-{yyyy}.csv', index=False)

    print("Done")


if __name__ == "__main__":
    from scripts.Globals import current_date

    day, month, year = current_date()
    web_scrapper(day, month, year)
