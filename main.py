import os
from datetime import date
from scripts.config import save_latex_variable
from scripts.WebScrapper import web_scrapper
from scripts.DataPlotter import data_plotter


day = date.today().day
month = date.today().month
year = date.today().year

dict_var = {'day': day, 'month': month, 'year': year}
# Saving variables for Latex
save_latex_variable(dict_var)

# Generate CSV Files
web_scrapper(day, month, year)

# Generate Plots
data_plotter(day, month, year)

# Creating Output Folder if not present
if not os.path.exists('output'):
    os.makedirs('output')

os.chdir('output')
# Generate Report
os.system("pdflatex ../DataReport.tex")
os.system("pdflatex ../DataReport.tex")
