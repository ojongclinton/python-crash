import matplotlib.pyplot as plt

initial_numbers = range(1,5001)
number_cubes = [x**3 for x in initial_numbers]

fig,ax = plt.subplots()
ax.scatter(initial_numbers,number_cubes,c='red',s=1)
# ax.plot(initial_numbers,number_cubes,c='red')
plt.show()
