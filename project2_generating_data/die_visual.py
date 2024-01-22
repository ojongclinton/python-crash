from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = []
labels = {'x':"Result",'y':'Frequency or result'}
title = "Results of Rolling Two D6 dice 1,000 Times"

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result+1)
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)

fig = px.bar(x=poss_results, y=frequencies, labels=labels, title=title)
fig.show()
