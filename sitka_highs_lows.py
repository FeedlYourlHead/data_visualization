import csv
from datetime import datetime

from matplotlib import pyplot as plt

# filename = 'data\sitka_weather_07-2018_simple.csv'
filename = 'data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6]) 
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use("bmh")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# print(highs)