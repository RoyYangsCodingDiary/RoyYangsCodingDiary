### Sample Output:

## 8/28/2023
#
#SPX: 4426.03
#DJI: 34441.64
#NASDAQ: 13695.4
#S&P/TSX: 19900.31
#VIX: 16.24
#USD/CAD: 1.3597
#EUR/USD: 1.0824
#USD/CNY: 7.2895
# 
#US 1 Month Yield: 5.40%
#US 3 Month Yield: 5.46%
#US 6 Month Yield: 5.59%
#US 1 Year Yield: 5.46%
#US 2 Year Yield: 5.00%
#US 3 Year Yield: 4.69%
#US 5 Year Yield: 4.37%
#US 7 Year Yield: 4.32%
#US 10 Year Yield: 4.19%
#US 30 Year Yield: 4.28%
# 
#Gold Spot:	$1,925.17, 0.26% from last close $1,920.23
#Palladium:	$1,247.50, -0.87% from last close $1,258.50
#Platinum Spot:	$972.00, 0.26% from last close $969.50
#Silver Spot:	$24.29, 0.04% from last close $24.28
#Natural Gas:	$2.55, -1.16% from last close $2.58
#Heating Oil:	$84.54, 0.0% from last close $84.54
#Oil (Brent):	$84.39, -0.04% from last close $84.42
#Oil (WTI):	$80.05, 0.1% from last close $80.10
#Aluminium:	$2,155.85, -0.07% from last close $2,155.85
#Lead Spot:	$2,177.00, -0.81% from last close $2,177.00
#Nickel Spot:	$20,886.50, 2.41% from last close $20,886.50
#Zinc Spot:	$2,375.25, 0.52% from last close $2,375.25
#Cotton Spot:	$0.86, -0.8% from last close $0.87
#Oats Spot:	$4.81, 0.57% from last close $4.83
#Coffee Spot:	$1.53, -0.97% from last close $1.52
#Cocoa Spot:	$2,785.00, 1.98% from last close $2,782.00
#Lean Hog Spot:	$0.82, 2.54% from last close $0.82
#Corn Spot:	$4.76, -0.68% from last close $4.79
#Feeder Cattle:	$2.50, 1.18% from last close $2.50
#Milk Spot:	$17.21, 0.06% from last close $17.20
#Orange Juice:	$3.19, -1.65% from last close $3.22
#Soybeans Spot:	$13.91, -0.3% from last close $13.95
#Wheat Spot:	$228.25, -1.93% from last close $228.75
#Sugar Spot:	$0.26, 2.93% from last close $0.26
# 
#### Holidays
#United Kingdom - Bank Holiday
#
#### Speeches
#BCB Focus Market Readout at 07:25
#German Buba President Nagel Speaks at 08:00
#German Buba Balz Speaks at 12:00
#
#### Economic Releases Today
#01:00: JPY Coincident Indicator (MoM) at 0.8%, missing consensus of 0.9% vs. previous 0.1%
#01:00: JPY Leading Index (MoM) at -0.2%, at consensus of -0.2% vs. previous 1.1%
#01:00: JPY Leading Index at 108.9, at consensus of 108.9 vs. previous 109.2
#04:00: EUR M3 Money Supply (YoY) (Jul) at -0.4%, missing consensus of 0.0% vs. previous 0.6%
#04:00: EUR Loans to Non Financial Corporations (Jul) at 2.2%, missing consensus of 2.5% vs. previous 3.0%
#04:00: EUR Private Sector Loans (YoY) at 1.3%, missing consensus of 1.4% vs. previous 1.7%
#07:30: BRL Bank lending (MoM) (Jul) at -0.2%, missing consensus of -0.1% vs. previous 0.1%
#08:55: EUR French 12-Month BTF Auction at 3.631% vs. previous 3.639%
#08:55: EUR French 3-Month BTF Auction at 3.664% vs. previous 3.684%
#08:55: EUR French 6-Month BTF Auction at 3.671% vs. previous 3.658%
#10:30: USD Dallas Fed Mfg Business Index (Aug) at -17.2, beating consensus of -21.6 vs. previous -20.0
#11:30: USD 2-Year Note Auction at 5.024% vs. previous 4.823%
#11:30: USD 6-Month Bill Auction at 5.350% vs. previous 5.295%
#13:00: USD 3-Month Bill Auction at 5.340% vs. previous 5.300%
#13:00: USD 5-Year Note Auction at 4.400% vs. previous 4.170%
#19:01: GBP BRC Shop Price Index (YoY) at 6.9% vs. previous 7.6%
#19:30: JPY Jobs/applications ratio (Jul) at 1.29, missing consensus of 1.30 vs. previous 1.30
#19:30: JPY Unemployment Rate (Jul) at 2.7%, beating consensus of 2.5% vs. previous 2.5%
#23:35: JPY 2-Year JGB Auction releasing soon, previous figure at -0.062% 
# 
#### M&A Activity: 
# - M&A also in the headlines again following a busy Friday afternoon, with weekend report FTC pausing its challenge to the ~$28B takeover of HZNP by AMGN to allow for settlement talks.
#### Headlines: 
# - There is (as has become typical) some focus today on China, specifically the raft of stimulus and reform measures Beijing announced this weekend, though the moves seemed to underwhelm and China's stock market pared gains after opening notably higher.
#- China increases product export quotas: Platts reports that its sources say China has issued additional oil
#- product export quotas, though no details were available on the volume of those new quotas. The article quotes analysts arguing Beijing's move may be aimed at supporting domestic industrial activities and could help increase China's crude imports as well.
#- Shell and Total looking for offshore opportunities near Namibi
#- Federal Reserve H.8 data from last week showed a drop in securities' balance and higher loan balance compared to the prior week. Commercial real estate loans added $2.3B while consumer loans inched $0.5B higher. Other loans shed $0.3B. Deposits declined $48.8B as large
#- time deposits rose $13.7B with core deposits declining by $62.5B.

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import datetime as dt
import math
import warnings
warnings.simplefilter("ignore")

# Function
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

def write_indicator_commentary(row):
    time = str(row["Time"])
    cur = str(row["Cur"])
    event = str(row["Event"])
    actual = str(row["Actual"])
    if actual == "Missing":
        actual_float = np.nan
    else:
        actual_float = float(row["Actual"].replace("%",""))
    
    forecast = str(row["Forecast"])
    if forecast == "Missing":
        forecast_float = np.nan
    else:
        forecast_float = float(row["Forecast"].replace("%",""))

    previous = str(row["Previous"])
    if previous == "Missing":
        previous_float = np.nan
    else:
        previous_float = float(row["Previous"].replace("%",""))

    if actual_float == "Missing":
        actual_vs_forecast = ""
    elif actual_float > forecast_float:
        actual_vs_forecast = "beating consensus of"
    elif actual_float < forecast_float:
        actual_vs_forecast = "missing consensus of"
    else:
        actual_vs_forecast = "at consensus of"
        
    
    if actual == "Missing":
        if forecast == "Missing":
            return f"{time}: {cur} {event} releasing soon, previous figure at {previous}"
        else:
            return f"{time}: {cur} {event} releasing soon, forecasted at {forecast} vs. previous {previous}"
    else:
        if forecast == "Missing":
            return f"{time}: {cur} {event} at {actual} vs. previous {previous}" 
        else:
            return f"{time}: {cur} {event} at {actual}, {actual_vs_forecast} {forecast} vs. previous {previous}"

# Yahoo Finance Data
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

# Bond Data
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

# Commodities
commodities_df = pd.read_html("https://markets.businessinsider.com/commodities/realtime-list")[0]
commodities_df = commodities_df.drop(columns=commodities_df.columns[-1])
commodities_df.columns = ["Commodity", "Last", "Previous Close", "%", "Absolute", "Trade Time", "Unit"]
commodities_df = commodities_df.dropna(subset=["Commodity"])
commodities_df = commodities_df.reset_index(drop=True)
commodities_df["Commodity"] = commodities_df["Commodity"].str.replace(" \(Henry Hub\)", "")

### Economic Events
with urlopen(Request(url = "https://www.investing.com/economic-calendar/", headers={'User-Agent': 'Mozilla/5.0'})) as response:
        webpage = response.read()
economic_events = pd.read_html(webpage)[2]
economic_events.columns = ["Time", "Cur", "Importance", "Event", "Actual", "Forecast", "Previous", "Extra1", "Extra2"]
economic_events = economic_events.drop(columns=["Extra1", "Extra2"], index=0)

if len(list(economic_events[economic_events["Importance"] == "Holiday"]["Event"].drop_duplicates())) == 0:
    holidays = "No market holidays today"
else:
    holidays = "\n".join(list(economic_events[economic_events["Importance"] == "Holiday"]["Event"].drop_duplicates()))

speeches = economic_events[economic_events[["Actual", "Forecast", "Previous"]].isnull().all(axis=1)][["Time", "Event"]]
speeches["Final"] = economic_events["Event"].astype(str) + " at " + economic_events["Time"]
speeches_string = "\n".join(list(speeches["Final"]))

indicators = economic_events[~((economic_events["Event"].isin(speeches["Event"])) | (economic_events["Event"].isin(economic_events[economic_events["Importance"] == "Holiday"]["Event"].drop_duplicates())))].reset_index(drop=True)
indicators = indicators.fillna("Missing")
indicators["Commentary"] = indicators.apply(write_indicator_commentary, axis=1)
indicators_string = "\n".join(list(indicators["Commentary"]))

# Commentary
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

text_current = text_current + f"### Holidays\n{holidays}\n\n### Speeches\n{speeches_string}\n\n### Economic Releases Today\n{indicators_string}"
                 
text_current = text_current + " \n"
text_current = text_current + " \n"

ma_activity = input("M&A Activity? ")
cleaned_ma_activity = "\n".join([f"- {n}" for n in [ele.strip() for ele in ma_activity.split("-") if ele.strip() != ""]])
text_current = text_current + (f"### M&A Activity: \n {cleaned_ma_activity}\n")

text_current = text_current + " \n"

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
