from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# for index,item in enumerate(header_row):
#     print(index,item)
# print(header_row)

dates, highs,lows = [] , [], []
for rows in reader:
    try:
        high = int(rows[3])
        low = int(rows[4])
        current_date = datetime.strptime(rows[2], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    except Exception as e:
        print(e)
        print(f"Missing data for {current_date}")
    

# print(highs)  

plt.style.use('seaborn')
fig, ax =plt.subplots()
ax.plot(dates,highs, c='red',alpha=0.5)
ax.plot(dates,lows, c='blue',alpha=0.5)

ax.fill_between(dates,highs,lows, facecolor='blue', alpha=0.1)

ax.set_title("Daily high temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
