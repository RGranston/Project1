#imports
import pandas as pd
import stockdata as sd
import questionary



def ask_stock_preference():
    index = ["S&P 500", "Dow 30", "Custom"]
    result = questionary.select("Select stocks you want to scan", index).ask()
    if result == "Manual Selection":
        tickers = questionary.text("Enter tickers separated by comma. ex) MSFT,TSLA,KO,T").ask()
        tickers_list = tickers.split(",")
        return tickers_list
    else:
        return result

# Main Application
if __name__ == "__main__":

    # Ask stock preference
    stocks = ask_stock_preference()

    # Get stock data
    stocks_information_df = sd.get_stock_data(stocks)
    print(stocks_information_df.head())

    # Ask indicators they want to use to filter
    indicators = []
    indicator = True
    while indicator != "exit":
        indicator = ask_indicators()
        indicators.append(indicator)
    indicators.remove("exit")
    # Check the result
    print(indicators)

    # Apply selected indicators to selected stocks
    sd.apply_indicators(stocks, indicators)
