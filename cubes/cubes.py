import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

x_values_two = range(1, 5001)
y_values_two = [x**3 for x in x_values_two]

# Set the style.
plt.style.use('seaborn-v0_8-colorblind')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values)

# Set the title, and label the axes.
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of values", fontsize=14)

# Second subplot
fig_two, ax_two = plt.subplots()
ax_two.scatter(x_values_two, y_values_two)

# Set the title, and label the axes of the second subplot.
ax_two.set_title("Cubes, 5000", fontsize=24)
ax_two.set_xlabel("Value", fontsize=14)
ax_two.set_ylabel("Cube of values", fontsize=14)

plt.show()
