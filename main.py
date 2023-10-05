import os
from datetime import date
from config import save_latex_variable
from WebScrapper import web_scrapper
from DataPlotter import data_plotter


day = date.today().day
month = date.today().month
year = date.today().year

# dict_var = {'day': day, 'month': month, 'year': year}
# Saving variables for Latex
# save_latex_variable(dict_var)

# Generate CSV Files
# web_scrapper(day, month, year)

# Generate Plots
# data_plotter(day, month, year)

# Generate Report
os.system("pdflatex DataReport.tex")
