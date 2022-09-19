#imports
import pandas as pd
import stockdata as sd
import questionary
import sys
import os
import fire

# Ask stock preference
def ask_stock_preference():
    index = ["S&P 500", "Dow 30", "Custom"]
    result = questionary.select("Select stocks you want to scan", index).ask()
    if result == "Custom":
        tickers = questionary.text("Enter tickers separated by comma. ex) MSFT,TSLA,KO,T").ask()
        tickers_list = tickers.split(",")
        return tickers_list
    else:
        return result


# Filter good performing stocks as of today.
def filter_good_performance_stocks(data):
    # Pick up the last business day
    today = data.index[-1]
    # Drop all row except today
    todays_data = data[data.index == pd.to_datetime(today)]
    # Drop all tickers that has total_return less than SPY's total_return
    todays_performance_df = todays_data[todays_data['total_return'] > todays_data[todays_data['ticker'] == 'SPY']['total_return'][0]]
    sorted_df = todays_performance_df.sort_values('total_return', ascending=False)
    return sorted_df


# Main Application
def run():
    # Ask stock preference
    stocks = ask_stock_preference()    

    # Get stock data
    stocks_information_df = sd.get_stock_data(stocks)

    # Filter good performing (Total return more than SPY) stocks
    good_performance_df = filter_good_performance_stocks(stocks_information_df)

    if good_performance_df.empty != True:
        print(f"Stocks with total return greater than S&P500") #D
        print(good_performance_df[['ticker', 'close', 'total_return']]) #D - then add continue
    # End program if there is no stocks with better performance than SPY
    else:
        print("No stocks you selected matches the criteria")
        sys.exit("Today is not the day for long trade")        

    # Filter out with technical analysis
    # Passing Golden Cross
    filter_1_df = good_performance_df[good_performance_df['SMA 50'] >= good_performance_df['SMA 200']]
    # EMA 20 >= SMA 20
    filter_2_df = filter_1_df[filter_1_df['EMA 20'] >= filter_1_df['SMA 20']]
    # RSI >= 50
    filter_3_df = filter_2_df[filter_2_df['RSI'] >= 50]
    # Close Price >= EMA 20
    filter_4_df = filter_3_df[filter_3_df['close'] >= filter_3_df['EMA 20']]

    # Display the result
    for df in [filter_4_df, filter_3_df, filter_2_df, filter_1_df]:
        # Go through filters above and create priority
        if df.empty == True:    
            continue
        elif df.empty != True:
            # If the filters return more than 10 stocks, then limit number to top 10.
            df = df.iloc[0:10, :]
            print("List of Good trending stocks' tickers:", list(df['ticker'])) #D
            print() #D
            print("Some details of Good trending stocks") #D
            print(df[['ticker', 'close', 'total_return']]) #D
            saved_tickers = list(df['ticker'])
            break
        else:
            print("No stocks you selected matches the criteria")
            sys.exit("Today is not the day for long trade")


    # Store data in CSV database to visualize over Jupyter Lab
    sd.store_in_csv(stocks_information_df, saved_tickers)
    
    # Run voila in the terminal and open website
    os.system("voila display.ipynb")

# Run the main application.
if __name__ == "__main__":
    try:
        fire.Fire(run)
    except Exception as e:
        print(f"You have some error.\nError Code: {e}")