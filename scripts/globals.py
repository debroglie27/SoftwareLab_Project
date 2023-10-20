import os
from datetime import date


def save_latex_variable(tex_dict, mode):
    filename = 'scripts/texData.dat'
    with open(filename, mode) as file:
        for key, value in tex_dict.items():
            file.write(f"{key},{value}\n")


def check_folder(folder_name):
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(project_directory, folder_name)

    # Creating plots folder if folder does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


day = date.today().day
month = date.today().month
year = date.today().year

cricket_formats = ['t20i', 'odi', 'test']
player_types = ['batting', 'bowling', 'all-rounder']
