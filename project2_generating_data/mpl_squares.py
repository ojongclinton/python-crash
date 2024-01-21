import matplotlib.pyplot as plt

input_values = range(1,1001)
squares = [x**2 for x in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(input_values, squares,c=squares ,cmap=plt.cm.Blues, s=1)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)         
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)
# ax.plot(input_values,squares,linewidth=1)

ax.axis([0,1100,0,1_100_000])
plt.show()
