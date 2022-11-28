// Data Project 1 File for Roy Yang, ...

// Step 1: Rename old variables to new, simpler names
rename year yr
rename oil_price_br brent
rename oil_cons_usa oil_cons
rename oil_prod_usa oil_prod
rename share_pipelines share_pipe
rename gdp_real_usa gdp
rename pop_usa pop
rename cpi_all_usa cpi
rename ir_usa ir
rename employed_usa employed
rename unemploy_rate_usa unemployed
// New variable names: yr, brent, oil_cons, oil_prod, share_pipe, gdp, pop, cpi, ir, employed, unemployed

// Step 2: See data as visual tables, notices that there seems to be empty values
list yr brent oil_cons oil_prod share_pipe gdp pop cpi ir employed unemployed

// Step 3: Remove blank values from dataset
drop if yr == .
drop if brent == .
drop if oil_cons == .
drop if oil_prod == .
drop if share_pipe == .
drop if gdp == .
drop if pop == .
drop if cpi == .
drop if ir == .
drop if employed == .
drop if unemployed == .
// It seems we are only left with data from 1939 to 2022

// Step 4: Summarize details for each variable, except for "yr"
summarize brent, detail
summarize oil_cons, detail
summarize oil_prod, detail
summarize share_pipe, detail
summarize gdp, detail
summarize pop, detail
summarize cpi, detail
summarize ir, detail
summarize employed, detail
summarize unemployed, detail

// Step 5: Show frequency tables of each variable
tabulate brent
tabulate oil_cons
tabulate oil_prod
tabulate share_pipe
tabulate gdp
tabulate pop
tabulate cpi
tabulate ir
tabulate employed
tabulate unemployed

// Step 6: Generate box and whisker plots for each variable
graph hbox brent, title (Brent Oil Prices (USD per Barrel))
graph hbox oil_cons, title (US Oil Consumption(1000s of Barrels per Day))
graph hbox oil_prod, title (US Field Production of Crude Oil(1000s of Barrel per Day))
graph hbox share_pipe, title (US Pipeline Ton-Miles of Freight/Overall US Ton-Miles of Freight)
graph hbox gdp, title (Real GDP in millions of PPP adjusted 2011)
graph hbox pop, title (US Mid-Year Population (1000s))
graph hbox cpi, title (US Consumer Price Index)
graph hbox ir, title (US Nominal Interest Rates)
graph hbox employed, title (US Employment Level (1000s of Persons))
graph hbox unemployed, title (US Unemployment Rate)

// Step 7: Generate histograms for each variable
histogram brent, start (0) width (5) percent title (Brent Oil Prices (USD per Barrel)) note (bins of 5)
histogram oil_cons, start (0) width (500) percent title (US Oil Consumption(1000s of Barrels per Day)) note (bins of 500)
histogram oil_prod, start (0) width (500) percent title (US Field Production of Crude Oil(1000s of Barrel per Day)) note (bins of 500)
histogram share_pipe, start (0) width (0.02) percent title (US Pipeline Ton-Miles/Overall US Ton-Miles) note (bins of 0.02)
histogram gdp, start (0) width (500000) percent title (Real GDP in millions of PPP adjusted 2011) note (bins of 500000)
histogram pop, start (130000) width (10000) percent title (US Mid-Year Population (1000s)) note (bins of 10000)
histogram cpi, start (0) width (5) percent title (US Consumer Price Index) note (bins of 5)
histogram ir, start (0) width (1) percent title (US Nominal Interest Rates) note (bins of 1)
histogram employed, start (40000) width (5000) percent title (US Employment Level (1000s of Persons)) note (bins of 5000)
histogram unemployed, start (0) width (1) percent title (US Unemployment Rate) note (bins of 1)

// Step 8: Generate correlation table of all the available variables

correlate yr brent oil_cons oil_prod share_pipe gdp pop cpi ir employed unemployed

// Now it's time for the real data analysis
// First question to answer: Have past oil shocks significantly impacted the U.S. economy? 
// Find oil consumption as % of total US population per year, then find mean, median, standard deviation, quartiles, histogram, and time series line graph (to see how dependent Americans are on oil)
// We will first generate a new variable. Since oil_cons is in 1000s of barrel per day, we will convert it to 1000s of barrels per year (assuming no leap years) and divide it by the US mid-year population in 1000s

gen oil_cons_perc_pop = (oil_cons*365)/pop
// oil_cons_perc_pop represents an estimate of the average barrels of oil consumed per US citizen per year

summarize oil_cons_perc_pop, detail

// Generate Histogram
histogram oil_cons_perc_pop, start (8) width (1) percent title (Average Barrels of Oil Consumed per US Citizen Yearly) note (bins of 1)

// Generate Time Series Line Graph
line oil_cons_perc_pop yr, title(Barrels of Oil Consumption per US Citizen Over Time) ytitle(Average Barrels of Oil Consumed per US Citizen Yearly) xtitle(Year)

// Find correlation between CPI and Brent Oil Prices, make scatter plot (to see how oil prices and inflation relate to each other)
correlate cpi brent

scatter cpi brent, title(Relationship of Brent Prices and CPI) ytitle(CPI) xtitle(Brent Oil Prices)

// Make new variable employment rate = employment level / total US population and find correlation with brent oil prices, or CPI
// Note that employment level and US total population are both in 1000s of people, so there is no need for adjustments

gen employment_rate = employed/pop

summarize employment_rate, detail

// Find correlation
correlate employment_rate brent cpi
// Find covariance
correlate employment_rate brent cpi, covariance

// Generate Scatter Plots
scatter employment_rate brent, title(Relationship of Brent Prices and Employment) ytitle(Employment Rate (%)) xtitle(Brent Oil Prices)
scatter employment_rate cpi, title(Relationship of CPI and Employment) ytitle(Employment Rate (%)) xtitle(CPI)

// Could the inverse also be true? What is the relationship between unemployment rate and brent prices and CPI?
correlate unemployed brent cpi
scatter unemployed brent, title(Relationship of Brent Prices and Unemployment) ytitle(Unemployment Rate (%)) xtitle(Brent Oil Prices)
scatter unemployed cpi, title(Relationship of CPI and Unemployment) ytitle(Unemployment Rate (%)) xtitle(CPI)


// Find oil production as % of total oil consumption year over year, find average, and make a time series line chart (to find if the US is dependent on importing oil)
gen perc_prod_of_cons = oil_prod/oil_cons

summarize perc_prod_of_cons, detail
//Generate line chart
line perc_prod_of_cons yr, title(US Oil Production as % of US Oil Consumption Over Time) ytitle(US Oil Production as % of Oil Consumption) xtitle(Year)

// Second Question to Answer: Does the data support that current oil price fluctuations might cause another recession in the U.S.?
// Find relationship of Oil Prices and GDP
correlate brent gdp
// Generate scatter plot, but generate a new variable beforehand: Real GDP in billions of PPP adjusted 2011
gen gdp_bill = gdp/1000
scatter gdp_bill brent, title(Relationship of US Nominal GDP and Brent Oil Prices) ytitle(Real GDP in billions of PPP adjusted 2011) xtitle(Brent Oil Price (USD per Barrel))

// Redo GDP box and whisker plot with a more concise x-axis scale this time
graph hbox gdp_bill, title (Real GDP in billions of PPP adjusted 2011)
summarize gdp_bill, detail

// Find relationship between Brent Oil & Interest Rate, and relationship between Interest Rates and GDP
correlate brent ir gdp
// Generate scatter plots
scatter gdp_bill ir, title(Relationship of US Nominal GDP and Interest Rates) ytitle(Real GDP in billions of PPP adjusted 2011) xtitle(US Nominal Interest Rates)
scatter ir brent, title(Relationship of Nominal Rates and Brent Oil Prices) ytitle(US Nominal Interest Rates) xtitle(Brent Oil Price (USD per Barrel))

// Generate GDP growth variable
// Make duplicate of "yr" variable
gen year_gdp = yr
tsset year_gdp
// Generate new variable, which is equivalent to the previous year's gdp
gen gdplag = l.gdp

gen gdp_growth = (gdp - gdplag)/gdplag

// Correlate GDP growth with all other variables
correlate brent oil_cons oil_prod share_pipe gdp pop cpi ir employed unemployed gdp_growth

// Generate Brent price growth variable
gen brent_lag = l.brent

gen brent_growth = (brent - brent_lag)/brent_lag

// Generate time series line graph
line gdp_growth brent_growth yr, title(GDP Growth (%) and Growth of Brent Prices YoY) ytitle(Growth (%)) xtitle(Year)

// We're going to prove that oil has economic impacts on real wages/income, but wages/income was not provided in the same dataset, so we imported data from FRED (Link: https://fred.stlouisfed.org) "Real Median Personal Income in the United States, 2021 CPI-U-RS Adjusted Dollars, Annual, Not Seasonally Adjusted"

import excel "C:\Users\yangroy\Documents\wages_data_set.xlsx", sheet("Sheet1"
> ) firstrow

// Find US oil production as % of real wages

// Find US oil production as % of real wages
rename year yr
rename oil_price_br brent
rename oil_cons_usa oil_cons
rename oil_prod_usa oil_prod
rename share_pipelines share_pipe
rename gdp_real_usa gdp
rename pop_usa pop
rename cpi_all_usa cpi
rename ir_usa ir
rename employed_usa employed
rename unemploy_rate_usa unemployed
rename real_med_income income

correlate income oil_cons oil_prod

scatter income oil_cons, title(Oil Consumption and its Impact on Real Median Income) ytitle(US Real Median Personal Income (USD)) xtitle(US Oil Consumption (1000s of Barrels))

scatter income oil_prod, title(Oil Production and its Impact on Real Median Income) ytitle(US Real Median Personal Income (USD)) xtitle(US Oil Production (1000s of Barrels))

// We will define demand shocks in oil as any consumption over the average oil consumption, filter out GDP for those years, and then find details for those years and compare them to unfiltered GDP
summarize oil_cons, detail

//We now know that the average is 10135.39, so we use that to generate a new variable that filters out GDP (in billions) for any demand shocks
gen oil_cons_shocks = gdp/1000 if oil_cons >= 10135.39
gen gdp_bill = gdp/1000
summarize oil_cons_shocks, detail
summarize gdp_bill, detail
// Generate box plot
graph hbox gdp_bill, title (GDP in Billions)
graph hbox oil_cons_shocks, title (GDP in Billions for years with Positive Demand Shocks in Oil)

// To answer question 3, we will import a new dataset
import excel "C:\Users\yangroy\Documents\data_question_2.xlsx
> ", sheet("Sheet1") firstrow

line oil_price_br year, title(Oil Prices over Time) ytitle(Brent Oil Prices) xtitle(Year)
 
 line gdp_growth1970 year_growth_1970, title(GDP Growth from 1970 to 1975) ytitle(Brent Oil Prices) xtitle(Year)
 scatter gdp_growth1970 year_growth_1970, title(GDP Growth from 1970 to 1975) ytitle(Brent Oil Prices) xtitle(Year)

 line gdp_growth_2003 year_growth_2003, title(GDP Growth from 2003 to 2009) ytitle(Brent Oil Prices) xtitle(Year)
 scatter gdp_growth_2003 year_growth_2003, title(GDP Growth from 2003 to 2009) ytitle(Brent Oil Prices) xtitle(Year)

summarize oil_price_1970, detail
summarize oil_price_2008, detail
summarize oil_price_2020, detail

sysuse auto, clear

foreach x in gdp_1970 oil_price_1970 gdp_2008 oil_price_2008 oil_price_br oil_price_2020{
    sum `x'
    display "Coefficient of Variation = " r(sd)/r(mean)
}
