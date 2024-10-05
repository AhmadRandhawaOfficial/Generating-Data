import matplotlib.pyplot as plt

"""x_values = [2, 3, 4, 5, 6,]
y_values = [4, 9, 16, 25, 36]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
"""

# using a colormap and Calculating the data automatically.
a_values = list(range(1, 101))
b_values = [a ** 2 for a in a_values]

plt.scatter(a_values, b_values, c=b_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.title("Squares", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Squares", fontsize=14)

# Set the range for each axis.
plt.axis([0, 110, 0, 11000])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()

