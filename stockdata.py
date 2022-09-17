#imports
import pandas as pd
from technical_indicators import calculate_technical_indicators
import datetime as dt
from yahoo_fin import stock_info as si
from functools import reduce

# Get stock data
def get_stock_data(stocks):
    # Set start date and end date
    start=dt.datetime.now() - dt.timedelta(days=1095)
    end=dt.datetime.now()

    # Get SPY Data
    spy_df = si.get_data('SPY', start_date=start, end_date=end)
    spy_df['total_return'] = (1 + spy_df['close'].pct_change()).cumprod()

    # Conditions: S&P500 or DOW30 or Custom
    if stocks == "S&P 500":
        sp500_tickers = si.tickers_sp500()
        # Get Data
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in sp500_tickers
            }
        ### This data looks like a dictionary
        ### { keys : values } = { tickers : pandas df } 
        ### For example:
        ###   price_data_dictionary['AAPL'] returns a dataframe that has columns as "open, high, low, close, adjclose, volume and ticker"

        # Calculate technical indicators and add columns
        calculate_technical_indicators(price_data_dictionary, sp500_tickers)

        # Make a dataframe that contains all ticker's information
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())
        ### reduce() function works similar to for loop.
        ### reduce(function, sequence)
        ### For this one, function is "pd.concat([x,y], axis=0)"
        ### For this one, sequence is taking x (= first value) and y (= next value) from price_data_dictionary, which is a pandas DataFrame
        

    elif stocks == "Dow 30":
        dow30_tickers = si.tickers_dow()
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in dow30_tickers
            }

        # Calculate technical indicators and add columns
        calculate_technical_indicators(price_data_dictionary, dow30_tickers)

        # Make a dataframe that contains all ticker's information        
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())


    else:
        price_data_dictionary = {
            ticker: si.get_data(ticker, start_date=start, end_date=end) for ticker in stocks
        }

        # Calculate technical indicators and add columns
        calculate_technical_indicators(price_data_dictionary, stocks)

        # Make a dataframe that contains all ticker's information
        df = reduce(lambda x, y: pd.concat([x,y], axis=0), price_data_dictionary.values())
    
    # Combine df with SPY performance
    final_df = pd.concat([df, spy_df], axis=0)
    return final_df



# Put Data in SQL database for easier use
def store_in_sql_tables(combined_df, stock_tickers):

    return
