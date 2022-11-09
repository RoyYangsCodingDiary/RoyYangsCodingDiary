#!/usr/bin/env python

# Completed: November 9, 2022
# This is a project guided by DataCamp

import pandas as pd
import matplotlib.pyplot as plt

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create Dictionary with Years and Durations
movie_dict = {"years": years, "durations": durations}
print(movie_dict)

# Convert Dictionary to Pandas DataFrame
durations_df = pd.DataFrame(movie_dict)
print(durations_df)

# Visualize Dataframe with Line Chart
fig = plt.figure()
plt.plot(years, durations)
plt.title("Netflix Movie Durations 2011-2020")
plt.show()
plt.clf()

# Part 2: Importing Another Dataset from a CSV file
netflix_df = pd.read_csv("datasets/netflix_data.csv")
print(netflix_df.iloc[0:5])

# Filter for only Movies, excludes TV shows
netflix_df_movies_only = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies_col_subset = netflix_df_movies_only[["title", "country", "genre", "release_year", "duration"]]
print(netflix_movies_col_subset.iloc[0:5])

# Create Scatter Plot
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"])
plt.title("Movie Duration by Year of Release")
plt.show()
plt.clf()

# Filter for Movies Shorter than 60 Minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]
print(short_movies.iloc[0:20])

# Add Colours to our Scatter Plot
colors = []
for label, row in netflix_movies_col_subset.iterrows() :
    if row["genre"] == "Children" :
        colors.append("red")
    elif row["genre"] == "Documentaries" :
        colors.append("blue")
    elif row["genre"] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
print(colors[0:9])

# Make Scatter Plot with Colours and Styling this Time
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies_col_subset["release_year"], netflix_movies_col_subset["duration"], color = colors)
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.show()
plt.clf()

