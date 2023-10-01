import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

curr_date = date.today()
day = curr_date.day
month = curr_date.month
year = curr_date.year

cricket_formats = ['t20i', 'odi', 'test']
player_types = ['batting', 'bowling', 'all-rounder']

basic_url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/'

for cricket_format in cricket_formats:
    for player_type in player_types:
        url = basic_url + cricket_format + '/' + player_type
        page = requests.get(url)

        soup = BeautifulSoup(page.text, 'html.parser')
        table = soup.find('table')
        table_titles = [title.text.strip() for title in table.find_all('th')]

        all_data = table.find_all('tr')
        row_1st = all_data[1].find_all('td')
        table_row_1st = ['1', row_1st[1].div.find_all('div')[1].a.div.text.strip(),
                         row_1st[2].div.text.strip(), row_1st[3].div.text.strip(),
                         row_1st[4].div.span.text.split('v')[0].strip()]

        df = pd.DataFrame(columns=table_titles)
        length = len(df)
        df.loc[length] = table_row_1st

        for index, row in enumerate(all_data[2:]):
            data = row.find_all('td')
            table_row = [f'{index+2}', data[1].a.text.strip(),
                         data[2].find_all('span')[1].text.strip(), data[3].text.strip(),
                         data[4].text.split('v')[0].strip()]

            length = len(df)
            df.loc[length] = table_row

        if not os.path.exists("./csv"):
            os.makedirs("./csv")

        df.to_csv(f'./csv/{cricket_format}_{player_type}_{day}-{month}-{year}.csv', index=False)
