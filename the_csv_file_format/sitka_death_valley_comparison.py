from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def get_weather_data(dates, highs, lows, filename, high_index, low_index, date_index):
    """Get the highs and lows from the data file."""
    dates = dates
    highs = highs
    lows = lows
    filename = filename
    high_index = high_index
    low_index = low_index
    date_index = date_index

    path = Path(filename)
    lines = path.read_text(encoding='utf-8').splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract the dates and the high and low temperatures.
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Get the weather data for Sitka
filename = "weather_data/sitka_weather_2021_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(dates, highs, lows, filename, 4, 5, 2)

# Plot the weather data for Sitka
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Get the weather data for Death Valley
filename = "weather_data/death_valley_2021_simple.csv"
dates, highs, lows = [], [], []
get_weather_data(dates, highs, lows, filename, 4, 5, 2)

# Plot the weather data for Death Valley
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format the plot.
title = "Comparison between Sitka and Death Valley"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()