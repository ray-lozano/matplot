import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() # subplots function generates one or more plots in the same figure.
ax.plot(squares, linewidth=3)        # plot method, plots data

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylable("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_arams(labelsize=14)

plt.show()