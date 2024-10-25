import pandas as pd
import numpy as np

def __init__(self, ticker, start: str, end: str):
    self.ticker = ticker
    self.start = start
    self.end = end

def get_data(self)-> pd.DataFrame:
    import yfinance as yf

    data = yf.download(self.ticker, self.start, self.end)
    data.dropna(axis = 0, how = "all", inplace = True)

    data.iloc[0,:].isna().sum()
    data.fillna(method = "ffill", inplace = True)
    return data

def get_techinal_indcitors(self, dataset: pd.DataFrame)-> pd.DataFrame:
    # Simple Moving Averages
    dataset['SMA_50'] = dataset['Close'].rolling(window=50).mean()
    dataset['SMA_200'] = dataset['Close'].rolling(window=200).mean()

    # Create MCAD
    dataset['EMA_12'] = dataset['Close'].ewm(span=12, adjust=False).mean()
    dataset['EMA_26'] = dataset['Close'].ewm(span=26, adjust=False).mean()

    # Create Bollinger Bonds
    dataset['Upper_Band'] = dataset['SMA_50'] + 2 * dataset['Close'].std()
    dataset['Lower_Band'] = dataset['SMA_50'] - 2 * dataset['Close'].std()

    # Create Exponential Moving Average
    dataset['EMA'] = dataset['Close'].ewm(span=20, adjust=False).mean()

    # Create Momentum
    dataset['Momentum'] = dataset['Close'].diff()

    return dataset