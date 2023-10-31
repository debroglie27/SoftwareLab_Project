import os
from datetime import date


CRICKET_FORMATS = ['t20i', 'odi', 'test']
PLAYER_TYPES = ['batting', 'bowling', 'all-rounder']
BAR_COLORS = {'t20i': 'green', 'odi': 'orange', 'test': 'purple', 'overall': 'cyan'}


def save_latex_variables(tex_dict: dict, mode: str) -> None:
    """
    Save key-value pairs from a dictionary to a LaTeX data file.

    Parameters:
    - tex_dict (dict): A dictionary containing key-value pairs to be saved.
    - mode (str): The file access mode ('w' for write, 'a' for append).

    This function is used to save key-value pairs from a dictionary to a LaTeX data file ('texData.dat').
    The file is opened in the specified mode, and each key-value pair is written to a new line in the file.

    Example usage:
    save_latex_variables({'day': 1, 'month': 1, 'year': 2023}, mode="w")  # Save date information to the LaTeX data file.
    """

    filename = 'scripts/texData.dat'
    with open(filename, mode) as file:
        for key, value in tex_dict.items():
            file.write(f"{key},{value}\n")


def check_folder(folder_name: str) -> str:
    """
    Check if a folder exists, and create it if it doesn't.

    Parameters:
    - folder_name (str): The name of the folder to check or create.

    Returns:
    - str: The path to the folder, whether it existed or was created.

    This function checks if a folder with the specified name exists within the project directory.
    If it doesn't exist, it creates the folder. The function returns the path to the folder.

    Example usage:
    folder_path = check_folder('plots')  # Check or create a 'plots' folder and get its path.
    """

    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(project_directory, folder_name)

    # Creating plots folder if folder does not exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


def current_date() -> tuple[int, int, int]:
    """
    Get the current date and save it for LaTeX use.

    Returns:
    - Tuple[int, int, int]: A tuple containing the current day, month, and year.

    This function retrieves the current date, including day, month, and year, and saves it for LaTeX to use.
    It returns the date information as a tuple.

    Example usage:
    day, month, year = current_date()  # Get the current date and save it for LaTeX use.
    """

    print("Fetching Current Date...")

    day = date.today().day
    month = date.today().month
    year = date.today().year

    # Saving the day, month and year for latex to use
    date_dict = {'day': day, 'month': month, 'year': year}
    save_latex_variables(date_dict, mode="w")

    print("Done")

    return day, month, year
