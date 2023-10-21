from scripts.globals import current_date
from scripts.WebScrapper import web_scrapper
from scripts.MergeCSV import merge_csv
from scripts.DataPlotter import data_plotter
from scripts.LatexCompiler import latex_compiler


if __name__ == "__main__":
    # Get Current Date
    day, month, year = current_date()

    # Generate CSV Files
    web_scrapper(day, month, year)

    # Merge CSV Files with same Cricket Format
    merge_csv(day, month, year)

    # Generate Plots
    data_plotter(day, month, year)

    # Compiling the Latex File
    latex_compiler()
