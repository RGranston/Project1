#imports
import pandas as pd
import technical_indicators as ti
import datetime as dt
import yahoo_fin as yf
from yahoo_fin import stock_info as si
from functools import reduce

# Get stock data
def get_stock_data(stock):
    # Set start date and end date
    start=dt.datetime.now() - dt.timedelta(days=365)
    end=dt.datetime.now()

    # Conditions: S&P500 or DOW30 or Custom
    if stock == "S&P 500":
        sp500_tickers = si.tickers_sp500()
        
        # Get Data
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in sp500_tickers
            }
        # This data looks like a dictionary
        # { keys : values } = { tickers : pandas df } 
        # For example:
        #   price_data_dictionary['AAPL'] returns a dataframe that has columns as "open, high, low, close, adjclose, volume and ticker"

        # Add "percent_change" column and "Cumprod" column in order to filter 10 best tickers for today
        for ticker in sp500_tickers:
            price_data_dictionary[ticker]["pct_change"] = price_data_dictionary[ticker]["close"].pct_change()
            price_data_dictionary[ticker]["total_return"] = (1 + price_data_dictionary[ticker]["pct_change"]).cumprod()

        # Make a dataframe that contains all ticker's information
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())
        

    elif stock == "Dow 30":
        dow30_tickers = si.tickers_dow()
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in dow30_tickers
            }
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())


    else:
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in stock
        }
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())
        return df


# Apply selected technical analysis
def apply_indicators(stocks, indicators):
    # Create empty dataframe
    stocks_df = pd.DataFrame()

    # Create Pandas dataframe that has columns for result of selected indicators


    return stocks_df