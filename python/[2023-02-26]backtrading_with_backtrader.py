#!/usr/bin/env python

# Import libraries
import pandas as pd
import backtrader as bt
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta
import datetime as dt
from backtrader.feeds import GenericCSVData

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

df1 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table1 = df1[0]
table1

# Select random sample of 5 companies from the S&P 500
np.random.seed(50)
sample = list(table1.sample(5)['Symbol'])
print(sample)
str1 = " ".join(sample)

today = dt.date.today()
start_date = today - timedelta(days=5*365)
end_date = today

df1 = yf.download(str1, start=start_date, end=end_date)['Close']
df1

# Get Data
data = pd.read_csv('AAPL.csv')
data

trade_data = bt.feeds.YahooFinanceCSVData(dataname='AAPL.csv')

class BuySellSignal(bt.observers.BuySell):
    plotlines = dict(
        buy=dict(marker='$\u21E7$', markersize=12.0),
        sell=dict(marker='$\u21E9$', markersize=12.0)
    )

# Dual Moving Average strategy
class SmaCross(bt.SignalStrategy):
    def log(self, txt, dt=None): # Log actions
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))  
        
    def __init__(self):
        sma_short, sma_long = bt.ind.SMA(period=10), bt.ind.SMA(period=20)
        self.crossover = bt.ind.CrossOver(sma_short, sma_long)
        self.log(f'Initial portfolio value of {self.broker.get_value():.2f}')

    def next(self):
        if not self.position:
            if self.crossover > 0: # If sma_short crosses sma_long above
                self.buy() # Long position
                self.log(f'BUY {self.getsizing()} shares of {self.data._name} at {self.data.close[0]}')
        elif self.crossover < 0: # Assumes in market and sma_short crosses below sma_long
            self.sell()
            self.log(f'Close LONG position of {self.position.size} shares '
                         f'of {self.data._name} at {self.data.close[0]:.2f}')

class BuyAndHold(bt.Strategy):
    def start(self):
        self.val_start = self.broker.get_cash()  # keep the starting cash

    def next(self):
        # Buy all the available cash
        size = int(self.broker.get_cash() / self.data)
        self.buy(size=size)

if __name__ == '__main__':
    cerebro = bt.Cerebro()
    # Set fixed position sizing
    cerebro.addsizer(bt.sizers.SizerFix, stake=20)
    cerebro.adddata(trade_data)
    # Set Initial Trading Capital and Trading Commissions
    cerebro.broker.setcash(10000.0)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.addstrategy(BuyAndHold)
    # Add Buy Sell Signals Observer to Cerebro
    cerebro.addobserver(bt.observers.Value)
    # Add Trading Statistics Analyzer
    cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')
    bt.observers.BuySell = BuySellSignal
    # Run Engine
    initial_portfolio_value = cerebro.broker.getvalue()
    cerebro.run()
    # Plot
    cerebro.plot()
    pnl = cerebro.broker.get_value() - initial_portfolio_value
    roi = ((cerebro.broker.get_value() / initial_portfolio_value) - 1)*100
    # Print balances
    print(f'Starting Portfolio Value: {initial_portfolio_value:.2f}')
    print(f'Final Portfolio Value: {cerebro.broker.get_value():.2f}')
    print(f'PnL: {pnl:.2f}')
    print(f'% Return: {roi:.2f}%')
