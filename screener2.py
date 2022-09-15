import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input("Enter a stock ticker symbol:")

print(stock)
startyear=2022
startmonth=1
startday=1

start=dt.datetime.now() - dt.timedelta(days=365)
end=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,end)

print(df)