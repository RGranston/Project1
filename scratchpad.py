# Ask user what type of technical analysis they're looking for
def ask_indicators():
    technical_analysis_indicators = [
        "Golden Cross", "Dead Cross", "20EMA and 20SMA", "RSI", "exit"
    ]
    result = questionary.select("Which indicator would you like to use to filter?", technical_analysis_indicators).ask()
    return result