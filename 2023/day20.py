from abc import ABC, abstractmethod
import numpy as np


class Module(ABC):
    def __init__(self, name: str, output_names: list):
        self.output_names = output_names
        self.output = []
        self.received_pulses = []
        self.name = name
        self.state = False

    def register_output(self, output):
        self.output.append(output)

    def initialize(self):
        self.state = False
        self.received_pulses = []

    def send(self, pulse):
        for module in self.output:
            # print("sending from", self.name, pulse, "to module", module.name)
            module.receive((self.name, pulse))

    def receive(self, pulse):
        self.received_pulses.append(pulse)

    @abstractmethod
    def process_pulses(self):
        pass


class FlipFlop(Module):
    def process_pulses(self):
        n_true = 0
        n_false = 0
        for pulse in self.received_pulses:
            _, pulse = pulse
            if pulse:
                n_true += 1
            else:
                n_false += 1
            if not pulse:
                self.state = not self.state
                self.send(self.state)
        self.received_pulses = []
        return n_true, n_false


class Conjunction(Module):
    def __init__(self, name: str, output_names:list):
        super(Conjunction, self).__init__(name, output_names)
        self.input = {}

    def register_input(self, input):
        for name in input:
            self.input[name] = False

    def process_pulses(self):
        n_true = 0
        n_false = 0
        for pulse in self.received_pulses:
            node, pulse = pulse
            if pulse:
                n_true += 1
            else:
                n_false += 1
            if node not in self.input.keys():
                print("Error")
            self.input[node] = pulse
            table = [v for v in self.input.values()]
            print(table, self.input.keys())
            if all(table):
                self.send(False)
            else:
                self.send(True)
        self.received_pulses = []
        return n_true, n_false


class Button(Module):
    def process_pulses(self):
        n_true = 0
        n_false = 0
        for pulse in self.received_pulses:
            _, pulse = pulse
            self.send(pulse)
            if pulse:
                n_true += 1
            else:
                n_false += 1
        self.received_pulses = []
        return 0, 0


class Broadcaster(Module):
    def process_pulses(self):
        n_true = 0
        n_false = 0
        for pulse in self.received_pulses:
            _, pulse = pulse
            if pulse:
                n_true += 1
            else:
                n_false += 1
            self.send(pulse)
        self.received_pulses = []
        return n_true, n_false



MODULE_LIST = {"%": FlipFlop, "&": Conjunction, "broadcaster": Broadcaster}


def get_module(line):
    module = line.split(">")[0]
    outputs = line.split(">")[1].split(",")
    outputs = [output.strip("\n").strip(" ") for output in outputs]
    if "broadcaster" not in module:
        ty = module[0]
        name = module[1:].strip("-").strip(" ")
        print(name, outputs)
    else:
        ty = "broadcaster"
        name = "broadcaster"
    module_class = MODULE_LIST[ty]
    new_module = module_class(name, outputs)
    return new_module


def initialize_modules(module_list):
    print("Initializing")
    for module in module_list:
        output_names = module.output_names
        name = module.name
        for output_module in module_list:
            if output_module.name in output_names:
                module.register_output(output_module)
            if name in output_module.output_names and isinstance(module, Conjunction):
                module.register_input(output_module.name)


        module.send(False)
    for module in module_list:
        module.initialize()
    return module_list


def main():
    with open("input day20.txt") as f:
        lines = f.readlines()
    # create a list with the modules
    # for loop
    module_list = [get_module(line) for line in lines]
    input_module = Button("button", ["broadcaster"])
    module_list.append(input_module)
    module_list = initialize_modules(module_list)
    n_cycles = 1000
    n_true = 0
    n_false = 0
    for _ in range(n_cycles):
        # print("Starting cycles")
        input_module.send(False)
        unprocessed_pulses = []
        for module in module_list:
            for pulse in module.received_pulses:
                unprocessed_pulses.append((module.name, pulse))

        while len(unprocessed_pulses) != 0:
            for module in module_list:
                t, f = module.process_pulses()
                n_true += t
                n_false += f
                print(n_true, n_false, n_true * n_false)
            unprocessed_pulses = []
            for module in module_list:
                for pulse in module.received_pulses:
                    unprocessed_pulses.append(pulse)

        print(n_true, n_false, n_true * n_false)

if __name__ == '__main__':
    main()

#532698839 too low