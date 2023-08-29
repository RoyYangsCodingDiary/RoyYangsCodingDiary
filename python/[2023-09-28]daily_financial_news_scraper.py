import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import datetime as dt
import warnings
warnings.simplefilter("ignore")

class yahoo:
    def get_open(link):
        with urlopen(Request(url = link, headers={'User-Agent': 'Mozilla/5.0'})) as response:
            webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return float((soup.find('td', attrs={'class': 'Ta(end) Fw(600) Lh(14px)', 'data-test': 'OPEN-value'}).text).replace(",",""))
    def get_current(link):
        with urlopen(Request(url = link, headers={'User-Agent': 'Mozilla/5.0'})) as response:
            webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return float((soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text).replace(",",""))

def get_market_watch_intraday_quote(url):
    with urlopen(Request(url = url, headers={'User-Agent': 'Mozilla/5.0'})) as response:
        webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return "{:.2f}".format(float(soup.find('bg-quote', class_='value').get_text()))

yahoo_data = {
    "SPX":yahoo.get_open("https://ca.finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"),
    "DJI":yahoo.get_open("https://ca.finance.yahoo.com/quote/%5EDJI?p=%5EDJI"),
    "NASDAQ":yahoo.get_open("https://ca.finance.yahoo.com/quote/%5EIXIC?p=^IXIC&.tsrc=fin-srch"),
    "S&P/TSX":yahoo.get_open("https://ca.finance.yahoo.com/quote/%5EGSPTSE?p=%5EGSPTSE"),
    "VIX":yahoo.get_open("https://ca.finance.yahoo.com/quote/%5EVIX?p=^VIX&.tsrc=fin-srch"),
    "USD/CAD":yahoo.get_open("https://ca.finance.yahoo.com/quote/CAD=X?p=CAD=X&.tsrc=fin-srch"),
    "EUR/USD":yahoo.get_open("https://ca.finance.yahoo.com/quote/EURUSD=X?p=EURUSD=X&.tsrc=fin-srch"),
    "USD/CNY":yahoo.get_open("https://ca.finance.yahoo.com/quote/CNY=X?p=CNY=X&.tsrc=fin-srch")
}

bond_data = {
    "US 1 Month Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd01m?countryCode=BX"),
    "US 3 Month Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd03m?countryCode=BX"),
    "US 6 Month Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd06m?countryCode=BX"),
    "US 1 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd01y?countryCode=BX"),
    "US 2 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd02y?countryCode=BX"),
    "US 3 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd03y?countryCode=BX"),
    "US 5 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd05y?countryCode=BX"),
    "US 7 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd07y?countryCode=BX"),
    "US 10 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd10y?countryCode=BX"),
    "US 30 Year Yield":get_market_watch_intraday_quote("https://www.marketwatch.com/investing/bond/tmubmusd30y?countryCode=BX")
}

commodities_df = pd.read_html("https://markets.businessinsider.com/commodities/realtime-list")[0]
commodities_df = commodities_df.drop(columns=commodities_df.columns[-1])
commodities_df.columns = ["Commodity", "Last", "Previous Close", "%", "Absolute", "Trade Time", "Unit"]
commodities_df = commodities_df.dropna(subset=["Commodity"])
commodities_df = commodities_df.reset_index(drop=True)
commodities_df["Commodity"] = commodities_df["Commodity"].str.replace(" \(Henry Hub\)", "")

today = dt.datetime.today()
text_current = f"\n# {today.month}/{today.day}/{today.year}\n\n"

for key, value in yahoo_data.items():
    text_current = text_current + f"{key}: {value}\n"
    
text_current = text_current + " \n"

for key, value in bond_data.items():
    text_current = text_current + f"{key}: {value}%\n"
    
text_current = text_current + " \n"

for row in range(commodities_df.shape[0]):
    if len(commodities_df.loc[row, "Commodity"]) < 9:
        commodity = commodities_df.loc[row, "Commodity"] + " Spot"
    else:
        commodity = commodities_df.loc[row, "Commodity"]
    
    last_price = "${:,.2f}".format(commodities_df.loc[row, "Last"])
    previous_close = "${:,.2f}".format(commodities_df.loc[row, "Previous Close"])
    pct = float((commodities_df.loc[row, "%"])[:-1])
    text_current = text_current + f"{commodity}:\t{last_price}, {pct}% from last close {previous_close}\n"
    
text_current = text_current + " \n"

ma_activity = input("M&A Activity? ")
cleaned_ma_activity = "\n".join([f"- {n}" for n in [ele.strip() for ele in ma_activity.split("-") if ele.strip() != ""]])
text_current = text_current + (f"### M&A Activity: \n {cleaned_ma_activity}\n")

headlines = input("Headlines? ")
cleaned_headlines = "\n".join([f"- {n}" for n in [ele.strip() for ele in headlines.split("-") if ele.strip() != ""]])
text_current = text_current + (f"### Headlines: \n {cleaned_headlines}")

print(text_current)


### Some optional economics data

with urlopen(Request(url = "https://ca.investing.com/economic-calendar/", headers={'User-Agent': 'Mozilla/5.0'})) as response:
    webpage = response.read()
soup = BeautifulSoup(webpage, 'html.parser')
table = soup.find('table', attrs={'id': 'economicCalendarData'})
pd.read_html(table.text)




with urlopen(Request(url = "https://tradingeconomics.com/calendar", headers={'User-Agent': 'Mozilla/5.0'})) as response:
    webpage = response.read()
soup = BeautifulSoup(webpage, 'html.parser')
table = soup.find('table', {'id': 'calendar', 'class': 'table table-hover table-condensed'})
pd.read_html(table.text)



def get_fred(url):
    with urlopen(Request(url = url, headers={'User-Agent': 'Mozilla/5.0'})) as response:
        webpage = response.read()
    soup = BeautifulSoup(webpage, 'html.parser')
    as_of_date = soup.find('span', {'class': 'series-meta-value'}).text.replace(":","")
    value = soup.find('span', {'class': 'series-meta-observation-value'}).text
    return as_of_date, value

us_econ_data = {
    "Headline CPI":"https://fred.stlouisfed.org/series/CPIAUCSL",
    "Core CPI":"https://fred.stlouisfed.org/series/CPILFESL",
    "Fed Funds":"https://fred.stlouisfed.org/series/FEDFUNDS",
    "Unemp. Rate":"https://fred.stlouisfed.org/series/UNRATE"
}
