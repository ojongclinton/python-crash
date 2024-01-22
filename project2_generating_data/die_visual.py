from die import Die
import plotly.express as px

die = Die()
results = []
titles = {'x':"Result",'y':'Frequency or result'}

for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequencie = results.count(value)
    frequencies.append(frequencie)

fig = px.bar(x=poss_results, y=frequencies, labels=titles)
fig.show()
