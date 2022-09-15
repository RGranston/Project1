#imports
import pandas as pd
import stockdata as sd
import questionary

# Ask user what type of technical analysis they're looking for
def ask_indicators():
    technical_analysis_indicators = [
        "Golden Cross", "Dead Cross", "20EMA > 20SMA", "RSI > 50", "exit"
    ]
    result = questionary.select("Which indicator would you like to use to filter?", technical_analysis_indicators).ask()
    return result

# Main Application
if __name__ == "__main__":

    # Ask stock preference (for now, only Dow 30)
    stocks = sd.get_stock_data()
    # Check the result
    print(stocks)

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
