import matplotlib.pyplot as plt

# Populate the empty lists x, y below with numbers of your choice
# Both lists should have same number of values

x = []
y = []

# Plotting using pyplot module in Matplotlib library
plt.plot(x,y, marker = '*')
plt.title(f"Plot of {len(x)} points. ")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("my_plot.png")
