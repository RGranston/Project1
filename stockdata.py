#imports
import pandas as pd
import technical_indicators as ti
import datetime as dt
import yfinance as yf
from pandas_datareader import data as pdr

# Get stock data
def get_stock_data(ticker):

    # Copied screener2.py
    yf.pdr_override()

    stock = input("Enter a stock ticker symbol:")

    print(stock)
    startyear=2022
    startmonth=1
    startday=1

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
