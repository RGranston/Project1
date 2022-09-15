#imports
import pandas as pd
import technical_indicators as ti
import datetime as dt
import yahoo_fin as yf
from pandas_datareader import data as pdr
import pandas_datareader as web

# Get stock data
def get_stock_data():

    stock = input("Enter a stock ticker symbol:")

    print(stock)

    start=dt.datetime.now() - dt.timedelta(days=365)
    end=dt.datetime.now()

    df=pdr.get_data_yahoo(stock,start,end)
    return df

# Apply selected technical analysis
def apply_indicators(stocks, indicators):
    # Create empty dataframe
    stocks_df = pd.DataFrame()

    # Create Pandas dataframe that has columns for result of selected indicators


    return stocks_df

def sp500_data():
    start = dt.datetime.now() - dt.timedelta(days=365)
    end = dt.datetime.now()

    sp500_df = web.DataReader('^GSPC', 'yahoo', start, end)
    return sp500_df