# Project 1: Stock Screener

## Team 3 Members
Granston, Ryan
Pham, Kenny
Takahashi, Yu

## Project Descritpion
Screening tool to filter stocks based on technical indicators:
1. Analyze the Dow 30 using technical indicators.
2. Filter out ‘buys’.
3. Present the data to the user using visual tools.

## Research Questions to Answer
1. What stocks should be considered a buy?
2. Why are they being considered?
3. Where do we project them?

## Dataset to be Used
Yahoo Finance

## Rough Breakdown of Tasks
1. Use Yahoo Finance API to filter stocks from the Dow 30.
    - Can this be easily scaled up?
2. Use CLI (or web app) to ask the user what indicators they want to use.
3. Calculate 200-day SMA and 50-day SMA to figure out the golden cross.
4. Create indicators to filter stocks.  For example:
    - Filter: 20EMA > 20SMA
        - 20-Day EMA formula
            - Pandas EMA function
                - .ewm() explanation
                - EMA =  Closing price * multiplier + EMA (previous day) * (1-multiplier)
                - Multiplier for 20-day EMA:  (2/(20+1))= 0.0952
    - Filter: Open > 20SMA and Close > 20SMA
    - Filter: RSI > 50
        - Use TA-lib library’s RSI function
5. Display the filtered stocks with a summary of technicals and fundamentals.
6. Graph the stocks using hvplot.
7. Run a Monte Carlo simmulation for forecasting.