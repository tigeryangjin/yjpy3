# python notebook for Make Your Own Neural Network
# code for a 3-layer neural network, and code for learning the MNIST dataset
# (c) Tariq Rashid, 2016
# license is GPLv2
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special

# library for plotting arrays
import matplotlib.pyplot


# ensure the plots are inside this notebook, not an external window
# neural network class definition
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # set number of nodes in each input, hidden, output layer
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # link weight matrices, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.input_nodes, -0.5), (self.hidden_nodes, self.input_nodes))
        self.who = numpy.random.normal(0.0, pow(self.hidden_nodes, -0.5), (self.output_nodes, self.hidden_nodes))

        # learning rate
        self.lr = learning_rate

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


class InstanceNeuralNetwork:
    def __init__(self, p_input_nodes, p_hidden_nodes, p_output_nodes, p_learning_rate):
        # number of input, hidden and output nodes
        self.input_nodes = p_input_nodes
        self.hidden_nodes = p_hidden_nodes
        self.output_nodes = p_output_nodes
        # learning rate
        self.learning_rate = p_learning_rate
        # create instance of neural network
        self.n = NeuralNetwork(self.input_nodes, self.hidden_nodes, self.output_nodes, self.learning_rate)

    def training_data(self, file_path):
        # load the mnist training data CSV file into a list
        training_data_file = open(file_path, 'r')
        training_data_list = training_data_file.readlines()
        training_data_file.close()

        # train the neural network

        # epochs is the number of times the training data set is used for training
        epochs = 5

        for e in range(epochs):
            # go through all records in the training data set
            for record in training_data_list:
                # split the record by the ',' commas
                all_values = record.split(',')
                # scale and shift the inputs
                inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
                # create the target output values (all 0.01, except the desired label which is 0.99)
                targets = numpy.zeros(self.output_nodes) + 0.01
                # all_values[0] is the target label for this record
                targets[int(all_values[0])] = 0.99
                self.n.train(inputs, targets)
                pass
            return ' The ' + str(e) + 'th training is over.'
            pass
        return 'The training has been completed!'

    def test_data(self, file_path):
        # load the mnist test data CSV file into a list
        test_data_file = open(file_path, 'r')
        test_data_list = test_data_file.readlines()
        test_data_file.close()

        # test the neural network

        # scorecard for how well the network performs, initially empty
        scorecard = []

        # go through all the records in the test data set
        for record in test_data_list:
            # split the record by the ',' commas
            all_values = record.split(',')
            # correct answer is first value
            correct_label = int(all_values[0])
            # scale and shift the inputs
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            # query the network
            outputs = self.n.query(inputs)
            # the index of the highest value corresponds to the label
            label = numpy.argmax(outputs)
            # print('correct_label: ' + str(correct_label))
            # print('label:' + str(label))
            # print('outputs: \n' + str(outputs))
            # append correct or incorrect to list
            if label == correct_label:
                # network's answer matches correct answer, add 1 to scorecard
                scorecard.append(1)
            else:
                # network's answer doesn't match correct answer, add 0 to scorecard
                scorecard.append(0)

                image_array = numpy.asfarray(all_values[1:]).reshape((28, 28))
                matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
                # title = str(correct_label) + '|' + str(label)
                matplotlib.pyplot.title(str(correct_label) + '|' + str(label))
                matplotlib.pyplot.show()
                pass

            pass
        # calculate the performance score, the fraction of correct answers
        # return scorecard
        scorecard_array = numpy.asarray(scorecard)
        return "performance = ", scorecard_array.sum() / scorecard_array.size


test = InstanceNeuralNetwork(784, 200, 10, 0.1)
print(InstanceNeuralNetwork.training_data(test, "d:/Users/tiger/Documents/mnist/mnist_train.csv"))
print(InstanceNeuralNetwork.test_data(test, "d:/Users/tiger/Documents/mnist/mnist_test.csv"))
