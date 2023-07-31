import numpy
import matplotlib.pyplot

data_file = open("d:/Users/tiger/Documents/mnist/mnist_test.csv", 'r')
data_list = data_file.readlines()
data_file.close()
all_values = data_list[0].split(',')
image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
# matplotlib.pyplot.show()
scaled_input = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
# print(scaled_input)

# output nodes is 10 (example)
onodes = 10
targets = numpy.zeros(onodes) + 0.01
print(targets)
print(all_values[0])
targets[int(all_values[0])] = 0.99
