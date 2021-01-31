import matplotlib.pyplot as plt

class Layer:
    def __init__(self, sequence, operation=None, previous=None):
        self.sequence = sequence
        self.operation = operation
        self.previous = previous

    def guess_value(self, value, operation):
        if operation == "addition":
            return self.return_last_value() + value
        elif operation == "multiplication":
            return self.return_last_value() * value
        else:
            raise RuntimeError("Unknown layer type: {}".format(operation))

    def return_last_value(self):
        return self.sequence[len(self.sequence)-1]

    def __str__(self):
        return str(self.sequence)


def same_elements(numbers): # checks if a given list contains the same elements
    if len(set(numbers)) <= 1:
        return True
    else:
        return False


def return_layer(sequence, op): # returns a bottom layer
    layer = []
    for i in range(0, len(sequence)-1):
        e = 0
        if op == "addition":
            e = sequence[i+1] - sequence[i]
        elif op == "multiplication":
            if sequence[i] == 0:  # look into this
                e = 0
            else:
                e = sequence[i+1] / sequence[i]
        else:
            raise RuntimeError("Unknown layer type: {}".format(op))
        layer.append(e)
    return layer


def populate_bottom_layers(layers, sequence, operation='', previous_layer=None): # populates layers parameter with bottom layers
    layer_object = Layer(sequence, operation, previous_layer)
    if len(sequence) == 1 or same_elements(sequence):
        layers.append(layer_object)
        return
    populate_bottom_layers(layers, return_layer(
        sequence, "addition"), "addition", layer_object)
    populate_bottom_layers(layers, return_layer(
        sequence, "multiplication"), "multiplication", layer_object)


def return_possibilities(bottom_layers):  # prints all possibilities and returns a list of them
    poss_numbers = []
    for layer in bottom_layers:
        value = layer.return_last_value()
        while layer.previous is not None:
            value = layer.previous.guess_value(value, layer.operation)
            layer = layer.previous
        poss_numbers.append(value)
    return poss_numbers


if __name__ == "__main__":
    numbers = []
    file_name = "input.txt" # input("Enter file name:")
    seperator = ' ' # input("Enter seperator:")
    save_file = "output.txt" # input("Enter a file name to save results, press enter to skip:")
    if seperator == '\\n':
        seperator = f'\n'
    with open(file_name, 'r') as file:
        raw_file = file.read().strip()
        if seperator:
            numbers = list(map(int, raw_file.split(seperator)))
        else:
            numbers = list(map(int, raw_file))
    bottom_layers = []
    populate_bottom_layers(bottom_layers, numbers)
    possible_numbers = return_possibilities(bottom_layers)
    possible_numbers.sort()
    number_str = str(numbers).strip('[]').replace(", ", ' ') + ' -> '
    if save_file:
        with open(save_file, 'w') as file:
            file.write("All Calculated Possibilities\n")
            for p in possible_numbers:
                file.write(number_str+str(p)+'\n')
    else:
        print("All Calculated Possibilities")
        for p in possible_numbers:
            print(number_str+str(p))
    x_axis = [i for i in range(len(possible_numbers))]
    y_axis = possible_numbers
    plt.plot(x_axis, y_axis)
    plt.show()