# Autogenerate Report On ICC Men's Ranking

This is a Software Lab (CS699) Project where we generate a report on ICC Men's Ranking using techniques and tools like web scraping, plotting and latex.  
`ICC - International Cricket Council`

## Group Members
| Name       | Roll No. |
|------------|----------|
| Arijeet De | 23M0742  |
| A Asish    | 23M0759  |

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
For each `<cricket-format> (t20i, odi, test)` we have 3 csv files:
- <cricket-format>_batting_DD-MM-YYYY.csv
- <cricket-format>_bowling_DD-MM-YYYY.csv
- <cricket-format>_all-rounder_DD-MM-YYYY.csv

For each `<cricket-format>` we are merging these csv files into one. So we will have 3 merged csv files:
- overall_odi_DD-MM-YYYY.csv
- overall_t20i_DD-MM-YYYY.csv
- overall_test_DD-MM-YYYY.csv

So in total we now have `12 csv files`.


### Data Plotting
Using the csv files bar plots are created. From each csv file 2 plots are created.

* **First Plot:** Number of Players for each Cricket Team
* **Second Plot:** Average Rating of Players for each Cricket Team

So in total we now have `24 bar plots`.


### PDF Report Generation
Using `pdflatex` command the DataReport.tex file was compiled and converted to a pdf file.
The pdf file gets generated in the output folder.

### Conclusion
This project can be leveraged for ongoing analysis by consistently gathering data and subsequently conducting comprehensive evaluations to gain insights into players' long-term performance trends.
