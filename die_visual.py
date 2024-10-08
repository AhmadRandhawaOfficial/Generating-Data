from die import Die
import pygal

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analyzing the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Result of rolling on D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_label = "Frequency of result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
