import os
from scripts.config import save_latex_variable, day, month, year
from scripts.WebScrapper import web_scrapper
from scripts.DataPlotter import data_plotter


# Defining key value pairs that will be saved
dict_var = {'day': day, 'month': month, 'year': year}
# Saving key value pairs for Latex
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
