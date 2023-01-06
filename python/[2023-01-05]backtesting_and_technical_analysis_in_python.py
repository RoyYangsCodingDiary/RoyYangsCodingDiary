#!/usr/bin/env python
# Import libraries
import pandas as pd
import numpy as np
import bt
import talib
import yfinance as yf
from datetime import datetime as dt
from datetime import timedelta, date
import seaborn as sns
import matplotlib.pyplot as plt

# Download Data
get = yf.Ticker('^GSPC')
print(get.info.keys())
data_raw = get.history(period='max')
print(data_raw)

# Convert Raw Data into DataFrame and Convert the Indices to Datetime
spx = pd.DataFrame(data_raw)
spx.index = pd.to_datetime(spx.index)
print(spx.head())

# Delete some Unnecessary Columns
spx = spx.drop(['Dividends', 'Stock Splits'], axis=1)

# Check Integrity of Data
print(spx.isna().sum())
print(spx.dtypes)

# First, some technical indicators! 
# Before that, we need to set the timeframe for our S&P 500 datasets to 10 years and 5 years
today = dt.date.today()
_5yrs_ago = today - timedelta(days=5*365)
_10yrs_ago = today - timedelta(days=10*365)
data5yr = get.history(start=_5yrs_ago, end=today)
data10yr = get.history(start=_10yrs_ago, end=today)

# 50 and 200 day SMA and EMA for 5 yr data
data5yr['SMA50'] = talib.SMA(data5yr['Close'], timeperiod=50)
data5yr['SMA200'] = talib.SMA(data5yr['Close'], timeperiod=200)
data5yr['EMA50'] = talib.EMA(data5yr['Close'], timeperiod=50)
data5yr['EMA200'] = talib.EMA(data5yr['Close'], timeperiod=200)

# Plot
fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1, sharey=True)
fig = plt.figure(figsize=(20,15))
ax0.plot(data5yr.index, data5yr['SMA50'], color='y', label='50 Day SMA')
ax0.plot(data5yr.index, data5yr['SMA200'], color='c', label='200 Day SMA')
ax0.legend()
ax0.set_title('SMAs and EMAs Over the Past 10 Years')
ax0.set_ylabel('Close Price')

ax1.plot(data5yr.index, data5yr['EMA50'], color='y', label='50 Day EMA')
ax1.plot(data5yr.index, data5yr['EMA200'], color='c', label='200 Day EMA')
ax1.legend()
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price')

plt.show()
plt.clf()

# Set golden and death cross trading signals, 1 = long signal, 0 = neutral, -1 = sell signal
SMA50 = data5yr['SMA50']
SMA200 = data5yr['SMA200']
EMA50 = data5yr['EMA50']
EMA200 = data5yr['EMA200']

signal_SMA = SMA200.copy()
signal_SMA[SMA200.isnull()] = 0
signal_SMA[SMA50 >= SMA200] = 1  # Golden Cross
signal_SMA[SMA50 < SMA200] = -1
data5yr['SMA_signal'] = signal_SMA

signal_EMA = EMA200.copy()
signal_EMA[EMA200.isnull()] = 0
signal_EMA[EMA50 >= EMA200] = 1  # Golden Cross
signal_EMA[EMA50 < EMA200] = -1
data5yr['EMA_signal'] = signal_EMA

fig, (ax0, ax2) = plt.subplots(nrows=2, ncols=1)
fig = plt.figure(figsize=(20,15))
ax0.plot(data5yr.index, data5yr['SMA50'], color='y', label='50 Day SMA')
ax0.plot(data5yr.index, data5yr['SMA200'], color='c', label='200 Day SMA')
ax1 = ax0.twinx()
ax1.plot(data5yr.index, data5yr['SMA_signal'], color='r', linewidth=0.8, label='SMA Signal')
ax0.legend()
ax0.set_title('Golden and Death Crosses Over the Past 5 Years')
ax0.set_ylabel('Close Price')

ax2.plot(data5yr.index, data5yr['EMA50'], color='y', label='50 Day EMA')
ax2.plot(data5yr.index, data5yr['EMA200'], color='c', label='200 Day EMA')
ax3 = ax2.twinx()
ax3.plot(data5yr.index, data5yr['EMA_signal'], color='r', linewidth=0.8, label='EMA Signal')
ax2.legend()
ax2.set_xlabel('Date')
ax2.set_ylabel('Close Price')

plt.show()
plt.clf()

# 50 and 200 day SMA and EMA for 10 yr data
data10yr['SMA50'] = talib.SMA(data10yr['Close'], timeperiod=50)
data10yr['SMA200'] = talib.SMA(data10yr['Close'], timeperiod=200)
data10yr['EMA50'] = talib.EMA(data10yr['Close'], timeperiod=50)
data10yr['EMA200'] = talib.EMA(data10yr['Close'], timeperiod=200)

# Plot
fig, (ax0, ax1) = plt.subplots(nrows=2, ncols=1, sharey=True)
fig = plt.figure(figsize=(20,15))
ax0.plot(data10yr.index, data10yr['SMA50'], color='y', label='50 Day SMA')
ax0.plot(data10yr.index, data10yr['SMA200'], color='c', label='200 Day SMA')
ax0.legend()
ax0.set_title('SMAs and EMAs Over the Past 10 Years')
ax0.set_ylabel('Close Price')

ax1.plot(data10yr.index, data10yr['EMA50'], color='y', label='50 Day EMA')
ax1.plot(data10yr.index, data10yr['EMA200'], color='c', label='200 Day EMA')
ax1.legend()
ax1.set_xlabel('Date')
ax1.set_ylabel('Close Price')

plt.show()
plt.clf()

# Set golden and death cross trading signals, 1 = long signal, 0 = neutral, -1 = sell signal
SMA50_1 = data10yr['SMA50']
SMA200_1 = data10yr['SMA200']
EMA50_1 = data10yr['EMA50']
EMA200_1 = data10yr['EMA200']

signal_SMA_1 = SMA200_1.copy()
signal_SMA_1[SMA200_1.isnull()] = 0
signal_SMA_1[SMA50_1 >= SMA200_1] = 1  # Golden Cross
signal_SMA_1[SMA50_1 < SMA200_1] = -1
data10yr['SMA_signal'] = signal_SMA_1

signal_EMA_1 = EMA200_1.copy()
signal_EMA_1[EMA200_1.isnull()] = 0
signal_EMA_1[EMA50_1 >= EMA200_1] = 1  # Golden Cross
signal_EMA_1[EMA50_1 < EMA200_1] = -1
data10yr['EMA_signal'] = signal_EMA_1

fig, (ax0, ax2) = plt.subplots(nrows=2, ncols=1)
fig = plt.figure(figsize=(20,15))
ax0.plot(data10yr.index, data10yr['SMA50'], color='y', label='50 Day SMA')
ax0.plot(data10yr.index, data10yr['SMA200'], color='c', label='200 Day SMA')
ax1 = ax0.twinx()
ax1.plot(data10yr.index, data10yr['SMA_signal'], color='r', linewidth=0.8, label='SMA Signal')
ax0.legend()
ax0.set_title('Golden and Death Crosses Over the Past 10 Years')
ax0.set_ylabel('Close Price')

ax2.plot(data10yr.index, data10yr['EMA50'], color='y', label='50 Day EMA')
ax2.plot(data10yr.index, data10yr['EMA200'], color='c', label='200 Day EMA')
ax3 = ax2.twinx()
ax3.plot(data10yr.index, data10yr['EMA_signal'], color='r', linewidth=0.8, label='EMA Signal')
ax2.legend()
ax2.set_xlabel('Date')
ax2.set_ylabel('Close Price')

plt.show()
plt.clf()

# Define Technicals() with Various Methods
class Technicals:
    def SMA(self, data, period):
        self.data = data
        self.period = period
        return self.data.rolling(self.period).mean().to_frame()
    def ADX(self, high_data, low_data, close_data, period=14):
        self.high_data = high_data
        self.low_data = low_data
        self.close_data = close_data
        self.period = period
        return talib.ADX(self.high_data, self.low_data, self.close_data, timeperiod=self.period).to_frame()
    def RSI(self, data, period=14):
        self.data = data
        self.period = period
        return talib.RSI(self.data, timeperiod=self.period).to_frame()
    def BollingerBands(self, data, n_deviations, period=20):
        self.data = data
        self.n_deviations = n_deviations
        self.period = period
        upper, mid, lower = talib.BBANDS(self.data, nbdevup=self.n_deviations, nbdevdn=self.n_deviations, timeperiod=self.period)
        df1 = pd.DataFrame(upper.rename('upper'))
        df2 = df1.merge(mid.rename('middle'), left_index=True, right_index=True).merge(lower.rename('lower'), left_index=True, right_index=True)
        return df2

# Add Signals to 5 yr Data
SMA_short = Technicals().SMA(data5yr['Close'], 50)
SMA_long = Technicals().SMA(data5yr['Close'], 200)
ADX_data = Technicals().ADX(data5yr['High'], data5yr['Low'], data5yr['Close'])
RSI_data = Technicals().RSI(data5yr['Close'])
BBands_data = Technicals().BollingerBands(data5yr['Close'], 1)

class Signal:
    def Crossover(self, SMA_short, SMA_long, data):
        self.SMA_short = SMA_short
        self.SMA_long = SMA_long
        self.data = data
        SMA_crossover_signal = self.SMA_long.copy()
        SMA_crossover_signal[self.SMA_long.isnull()] = 0
        SMA_crossover_signal[self.SMA_short >= self.SMA_long] = 1
        SMA_crossover_signal[self.SMA_short < self.SMA_long] = -1
        combined_df = bt.merge(SMA_crossover_signal, self.data, self.SMA_short, self.SMA_long)
        combined_df.columns = ['SMA_signal', 'Price', 'SMA_short', 'SMA_long']
        return combined_df
    def ADX(self, ADX_series, data):
        self.ADX_series = ADX_series
        self.data = data
        ADX_signal = self.ADX_series.copy()
        ADX_signal[self.ADX_series.isnull()] = 0
        ADX_signal[self.ADX_series <= 25] = 0
        ADX_signal[(self.ADX_series > 25) & (self.ADX_series < 50)] = 0.5
        ADX_signal[self.ADX_series >= 50] = 1
        combined_df = bt.merge(self.data, ADX_signal)
        combined_df.columns = ['Price', 'ADX_signal']
        return combined_df
    def RSI(self, RSI_series, data):
        self.RSI_series = RSI_series
        self.data = data
        RSI_signal = self.RSI_series.copy()
        RSI_signal[self.RSI_series.isnull()] = 0
        RSI_signal[self.RSI_series > 70] = -1
        RSI_signal[self.RSI_series < 30] = 1
        RSI_signal[(self.RSI_series >= 30) & (self.RSI_series <= 70)] = 0
        combined_df = bt.merge(self.data, RSI_signal)
        combined_df.columns = ['Price', 'RSI_signal']
        return combined_df
    def BollingerBands(self, BBands_upper, BBands_lower, data):
        self.BBands_upper = BBands_upper
        self.BBands_lower = BBands_lower
        self.data = data
        BB_signal = self.BBands_upper.copy()
        BB_signal[self.BBands_upper.isnull()] = 0
        BB_signal[self.data > self.BBands_upper] = -1
        BB_signal[self.data < self.BBands_lower] = 1
        BB_signal[(self.data > self.BBands_lower) & self.data < self.BBands_upper] = 0
        combined_df = bt.merge(self.data, BB_signal)
        combined_df.columns = ['Price', 'BB_signal']
        return combined_df


def display_all_signals(price_data, SMA_short, SMA_long, ADX_data, RSI_data, BB_dataframe):
    SMA_signal = Signal().Crossover(SMA_short, SMA_long, price_data)['SMA_signal'].to_frame()
    ADX_signal = Signal().ADX(ADX_data, price_data)['ADX_signal'].to_frame()
    RSI_signal = Signal().RSI(RSI_data, price_data)['RSI_signal'].to_frame()
    BB_signal = Signal().BollingerBands(BB_dataframe['upper'], BB_dataframe['lower'], price_data)['BB_signal'].to_frame()
    signals = SMA_signal.merge(ADX_signal, left_index=True, right_index=True).merge(RSI_signal, left_index=True, right_index=True).merge(BB_signal, left_index=True, right_index=True)
    signals['signal_summary'] = signals.sum(axis=1)
    return signals

signals_df = display_all_signals(data5yr['Close'], SMA_short, SMA_long, ADX_data, RSI_data, BBands_data)

def plot_all_signals(signals_df, price_data):
    fig, [[ax0, ax1], [ax2, ax3]] = plt.subplots(nrows=2, ncols=2)
    fig = plt.figure(figsize=(20,15))

    ax0.plot(price_data.index, price_data, color='black', label='Close Price')
    ax4 = ax0.twinx()
    ax4.set_yticks([-1, 0, 1])
    ax4.plot(signals_df.index, signals_df['SMA_signal'], color='red', label='SMA Signal')
    ax4.legend()
    
    ax1.plot(price_data.index, price_data, color='black', label='Close Price')
    ax5 = ax1.twinx()
    ax5.set_yticks([0, 0.5, 1])
    ax5.plot(signals_df.index, signals_df['ADX_signal'], color='red', label='ADX Signal')
    ax5.legend()

    ax2.plot(price_data.index, price_data, color='black', label='Close Price')
    ax6 = ax2.twinx()
    ax6.set_yticks([-1, 0, 1])
    ax6.plot(signals_df.index, signals_df['RSI_signal'], color='red', label='RSI Signal')
    ax6.legend()
    
    ax3.plot(price_data.index, price_data, color='black', label='Close Price')
    ax7 = ax3.twinx()
    ax7.set_yticks([0, 0.5, 1])
    ax7.plot(signals_df.index, signals_df['BB_signal'], color='red', label='BB Signal')
    ax7.legend()

plt.rc('xtick', labelsize=5) 
plt.rc('ytick', labelsize=5) 
plot_all_signals(signals_df, data5yr['Close'])
plt.show()
plt.clf

# Display the sum of all signals vs. price, high signal = long, low signal = short

fig, ax0 = plt.subplots()
fig = plt.figure(figsize=(20,15))

ax0.plot(data5yr.index, data5yr['Close'], color='black')
ax1 = ax0.twinx()
ax1.plot(signals_df.index, signals_df['signal_summary'], color='red')
plt.show()
plt.clf()

# Backtest #1: Just checking if everything is working & this will set our benchmark
get_ipython().run_line_magic('matplotlib', 'inline')
bt_data = spx.drop(['Open', 'High', 'Low', 'Volume'], axis=1)

def backtestrun(data, strategy_name):
    bt_strategy = bt.Strategy(strategy_name, 
                          [bt.algos.RunMonthly(),
                           bt.algos.SelectAll(),
                           bt.algos.WeighEqually(),
                           bt.algos.Rebalance()])
    bt_test = bt.Backtest(bt_strategy, bt_data)
    bt_res = bt.run(bt_test)
    return bt_res

testrun = backtestrun(bt_data,'benchmark')

testrun.plot(title='Benchmark: Reinvesting in S&P 500 Monthly')
testrun.get_transactions() # Get trade details
testrun.display() # Get trade statistics

# Next steps: explore other backtesting libraries in Python
