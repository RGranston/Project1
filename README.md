# Project 1 Stock Screener
- Kenny Pham
- Ryan Granston
- Yu Takahashi

## Executive Summary
In this project we built a CLI application to filter through a stock index and display its findings on an interactive graph in a web browser.

## Required modules to run the app.py
**Installation required modules**

- `questionary`
- `datetime`
- `yahoo_fin`
- `requests_html`
- `functools`
- `TA-lib`
- `fire`
- `voila`

**Modules come with Anaconda destribution**

- `pandas`
- `sys`
- `plotly`
- `pathlib`
- `os`
- `csv`

## Instructions to install the modules
*Make sure to install all the modules in working environment!*

In order to install `TA-lib`, type `conda install -c conda-forge ta-lib` on GitBash or Terminal

In order to install `voila`, type `conda install -c conda-forge voila` on GitBash or Terminal

Type `pip install "module name"` on GitBash or Terminal to install all other modules

## Data Collection
To collect market data we used the Yahoo_fin api.  This allows us to pull up to date, relevant market data from Yahoo Finance. The application will prompt the user if they want to pull from the S&P 500, DOW 30 or use custom list.

![Data](/Images/yahoofin.PNG)

## Stock Filter
The filter we use looks for the 'golden cross' technical analysis indicator.

![Golden Cross](/Images/goldencross.PNG)

Rather than manually calculating the technical analysis functions for the filter we used TA Lib to automate the process.

![TALib](/Images/talib.PNG)

Here is the complete filter. It includes passing golden cross, simple moving averages, exponential moving averages, and the relative strength index.  This will give us our buy indicator.

![Filter](/Images/filter.PNG)

The stocks with our buy indicator are saved under 'Resources' as csv files.

## Presenting the Data
To present the data we used Jupyter Lab to build interactive graphs and post funamental analysis.

![CandlestickGraph](/Images/candlestick.PNG)

We then used Voila to display the graph and fundamentals in a web browser.

![Voila](/Images/voila.PNG)

## Analysis

The web browser will display each individual stock that had our buy indicator.  The graph will show our technical analysis, with fundamental analysis underneath.

![TA](/Images/enph.PNG)

![FA](/Images/fundamental.PNG)

## Notes
We are not giving financial advise.  Proceed at your own risk.