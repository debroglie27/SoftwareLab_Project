from scripts.WebScrapper import web_scrapper
from scripts.DataPlotter import data_plotter
from scripts.LatexCompiler import latex_compiler
from scripts.config import save_latex_variable, day, month, year


# Defining key value pairs that will be saved
dict_var = {'day': day, 'month': month, 'year': year}
# Saving key value pairs for Latex
save_latex_variable(dict_var)

# Generate CSV Files
web_scrapper(day, month, year)

# Generate Plots
data_plotter(day, month, year)

# Compiling the Latex File
latex_compiler()
