import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]  # plot the data on the y-axis.
plt.plot(input_values, squares,
          linewidth=5)  # By default, x-axis use 0,1,2,3,4; and if 1 value is given it behaves like y-axis.

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)
plt.show()

# Default values, linewidth=1.5, fontsize, lsbelsize=10, s=20, dpi=100, fig(6.4, 4.8)inches

