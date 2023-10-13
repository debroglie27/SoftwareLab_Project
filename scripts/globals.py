from datetime import date


def save_latex_variable(tex_dict, mode):
    filename = 'scripts/texData.dat'
    with open(filename, mode) as file:
        for key, value in tex_dict.items():
            file.write(f"{key},{value}\n")


day = date.today().day
month = date.today().month
year = date.today().year

cricket_formats = ['t20i', 'odi', 'test']
player_types = ['batting', 'bowling', 'all-rounder']
