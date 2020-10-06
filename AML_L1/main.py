import numpy
import matplotlib.pyplot as plt
import math

range = 1
first_number = -200
last_number = 300

x_values = numpy.arange(first_number, last_number, range)
y_values = [math.tanh(i) for i in x_values]

plt.plot(x_values, y_values, label='linear')
plt.show()
