import matplotlib.pyplot as plt

# Populate the empty lists x, y below with numbers of your choice
# Both lists should have same number of values

x = [2,6,10,18,25,34,45]
y = [0,7,12,19,27,19,50]

# Plotting using pyplot module in Matplotlib library
plt.plot(x,y, marker = '*')
plt.title(f"Plot of {len(x)} points. ")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("my_plot.png")
