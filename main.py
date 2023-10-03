from config import day, month, year
from WebScrapper import web_scrapper
from DataPlotter import data_plotter

# Generate CSV Files
web_scrapper(day, month, year)

# Generate Plots
data_plotter(day, month, year)
