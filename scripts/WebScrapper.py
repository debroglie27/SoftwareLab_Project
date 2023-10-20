import requests
import pandas as pd
from bs4 import BeautifulSoup
from scripts.globals import cricket_formats, player_types, save_latex_variable, check_folder


def web_scrapper(dd, mm, yyyy):
    base_url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/'

    check_folder('csv')

    pos1_player_names = {}

    for cricket_format in cricket_formats:
        for player_type in player_types:
            url = base_url + cricket_format + '/' + player_type
            page = requests.get(url)

            soup = BeautifulSoup(page.text, 'html.parser')
            table = soup.find('table')
            table_titles = [title.text.strip() for title in table.find_all('th')]

            all_data = table.find_all('tr')
            row_1st = all_data[1].find_all('td')

            # Position 1 Player Details
            pos1_player_name = row_1st[1].div.find_all('div')[1].a.div.text.strip()
            pos1_player_team = row_1st[2].div.text.strip()
            pos1_player_rating = row_1st[3].div.text.strip()
            pos1_player_best_rating = row_1st[4].div.span.text.split('v')[0].strip()

            # Storing Position 1 Player Details in a Dictionary
            pos1_player_names[f'{cricket_format}-{player_type}-name'] = pos1_player_name
            pos1_player_names[f'{cricket_format}-{player_type}-team'] = pos1_player_team
            pos1_player_names[f'{cricket_format}-{player_type}-rating'] = pos1_player_rating
            pos1_player_names[f'{cricket_format}-{player_type}-best-rating'] = pos1_player_best_rating

            table_row_1st = ['1', row_1st[1].div.find_all('div')[1].a.div.text.strip(),
                             row_1st[2].div.text.strip(), row_1st[3].div.text.strip(),
                             row_1st[4].div.span.text.split('v')[0].strip()]

            # Initialising the dataframe using table titles
            df = pd.DataFrame(columns=table_titles)

            # Adding the 1st row in the dataframe
            length = len(df)
            df.loc[length] = table_row_1st

            for index, row in enumerate(all_data[2:]):
                data = row.find_all('td')
                table_row = [f'{index+2}', data[1].a.text.strip(),
                             data[2].find_all('span')[1].text.strip(), data[3].text.strip(),
                             data[4].text.split('v')[0].strip()]

                # Adding the rows in the dataframe
                length = len(df)
                df.loc[length] = table_row

            df.to_csv(f'./csv/{cricket_format}_{player_type}_{dd}-{mm}-{yyyy}.csv', index=False)

    save_latex_variable(pos1_player_names, mode="a")


if __name__ == "__main__":
    from scripts.globals import day, month, year
    web_scrapper(day, month, year)
