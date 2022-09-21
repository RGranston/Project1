from yahoo_fin import stock_info as si
import datetime as dt

stock = input("Enter a stock ticker symbol:")

print(stock)

start=dt.datetime.now() - dt.timedelta(days=365)
end=dt.datetime.now()

df=si.get_data(stock,start,end)

print(df)