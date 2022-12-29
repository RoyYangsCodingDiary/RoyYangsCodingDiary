#!/usr/bin/env python
# Project Guided by DataCamp
# Analysis of Handwashing and its effects on childbirth death rates

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')
print(yearly)

yearly['proportion_deaths'] = yearly['deaths']/yearly['births']
clinic_1 = yearly[yearly['clinic'] == 'clinic 1']
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']
print(clinic_1)

ax = clinic_1.plot(x='year', y='proportion_deaths', label='Clinic 1')
clinic_2.plot(x='year', y='proportion_deaths', label='Clinic 2', ax=ax)

ax.set_ylabel('Proportion deaths')
plt.show()
plt.clf

monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])
monthly['proportion_deaths'] = monthly['deaths'] / monthly['births']
print(monthly.head())

ax = monthly.plot(x='date', y='proportion_deaths')
ax.set_ylabel('Proportion Deaths')

handwashing_start = pd.to_datetime('1847-06-01')

before_washing = monthly[monthly['date'] < handwashing_start]
after_washing = monthly[monthly['date'] >= handwashing_start]

ax= before_washing.plot(x='date', y='proportion_deaths', label='Before Hand Washing')
after_washing.plot(x='date', y='proportion_deaths', label='After Hand Washing', ax=ax)
ax.set_ylabel='Proportion deaths'

before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']
mean_diff = after_proportion.mean() - before_proportion.mean() 
mean_diff

# A bootstrap analysis of the reduction of deaths due to handwashing
boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
confidence_interval
