# Autogenerate Report On ICC Men's Ranking

This is a Software Lab (CS699) Project where we generate a report on ICC Men's Ranking and that too automatic.  
`ICC - International Cricket Council`

## Group Members
- Arijeet De (23M0742)
- A Asish (23M0759)

## Packages Used

- requests (2.31.0)
- beautifulsoup4 (4.12.2)
- pandas (2.1.1)
- matplotlib (3.8.0)
- pdflatex (0.1.3)

## Introduction

The entire project is divided into 5 steps:
- Fetching Current Date
- Web Scraping
- Merging CSV Files
- Data Plotting
- PDF Report Generation

### Fetching Current Date

The current day, month and year is retrieved: 
- For keeping track of csv files
- To use as date in latex

### Web Scraping

The data is collected from ICC's official website (9 Webpages):
- [T20i Batting Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/batting)
- [T20i Bowling Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/bowling)
- [T20i All-Rounder Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/t20i/all-rounder)
- [ODI Batting Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting)
- [ODI Bowling Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling)
- [ODI All-Rounder Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder)
- [Test Batting Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/test/batting)
- [Test Bowling Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/test/bowling)
- [Test All-Rounder Ranking Data](https://www.icc-cricket.com/rankings/mens/player-rankings/test/all-rounder)

The Data collected is stored inside a csv folder and data from each webpage is in separate csv files.
- t20i_batting_DD-MM-YYYY.csv
- t20i_bowling_DD-MM-YYYY.csv
- t20i_all-rounder_DD-MM-YYYY.csv
- odi_batting_DD-MM-YYYY.csv
- odi_bowling_DD-MM-YYYY.csv
- odi_all-rounder_DD-MM-YYYY.csv
- test_batting_DD-MM-YYYY.csv
- test_bowling_DD-MM-YYYY.csv
- test_all-rounder_DD-MM-YYYY.csv

`Note: Day, Month and Year are also specified to represent the date of web scraping.`

#### About The Data

Columns:
* Pos: Rank of Player
* Player: Name of Player
* Team: Team the Player belongs to
* Rating: Rating of Player (out of 1000)
* Career Best Rating: Career Best Rating of Player (out of 1000)


### Merging CSV Files

### Data Plotting
Using the csv files bar plots are created. From each csv file 2 plots are created.

* First Plot: Number of Players for each Cricket Team
* Second Plot: Average Rating of Players for each Cricket Team

### PDF Report Generation

### Conclusion