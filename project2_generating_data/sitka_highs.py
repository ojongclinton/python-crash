from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
# for index,item in enumerate(header_row):
#     print(index,item)
# print(header_row)

highs = []
for rows in reader:
    high = int(rows[4])
    highs.append(high)

print(highs)  

plt.style.use('seaborn')
fig, ax =plt.subplots()
ax.plot(highs, c='red')

ax.set_title("Daily high temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
