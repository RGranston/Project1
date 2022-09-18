### IMPORTANT ###
# Install TA-lib library by using the code below on git bash.
#   "conda install -c conda-forge ta-lib"
import talib as ta

# Calculate 200-day SMA
def calculate_200_sma(close):
    result = ta.SMA(close, timeperiod=200)
    return result

# Calculate 50-day SMA
def calculate_50_sma(close):
    result = ta.SMA(close, timeperiod=50)
    return result

# Calculate 20-day SMA
def calculate_20_sma(close):
    result = ta.SMA(close, timeperiod=20)
    return result

# Calculate 20-day EMA
def calculate_20_ema(close):
    result = ta.EMA(close, timeperiod=20)
    return result

# Calculate RSI
def calculate_rsi(close):
    result = ta.RSI(close, timeperiod=14)
    return result

def calculate_technical_indicators(data_dict, ticker_list):
    for ticker in ticker_list:
            data_dict[ticker]["pct_change"] = data_dict[ticker]["close"].pct_change().dropna()
            data_dict[ticker]["total_return"] = (1 + data_dict[ticker]["pct_change"]).cumprod()
            data_dict[ticker]["SMA 200"] = calculate_200_sma(data_dict[ticker]["close"])
            data_dict[ticker]["SMA 50"] = calculate_50_sma(data_dict[ticker]["close"])
            data_dict[ticker]["SMA 20"] = calculate_20_sma(data_dict[ticker]["close"])
            data_dict[ticker]["EMA 20"] = calculate_20_ema(data_dict[ticker]["close"])
            data_dict[ticker]["RSI"] = calculate_rsi(data_dict[ticker]["close"])