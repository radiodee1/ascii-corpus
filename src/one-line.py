#!/bin/env python3 
import argparse
import random

json_prompt = {
        'label': 'json-three-lines-alpaca',
        'slots': 3,
        'text' : {
            'input': '{}',
            'instruction' : '{}',
            'output': '{}'
            }
        }



class Generate:
    def __init__(self):

        self.lines = 0
        self.integers = 10
        self.name = ""
        self.verbose = False
        self.prompt = False
        self.bag = []

    def test_output(self):
        print('test_output')

    def substitute_in_json(self, question, statement, output):
        x = json_prompt.copy()['text']
        x['input'] = x['input'].format(statement)
        x['instruction'] = x['instruction'].format(question)
        x['output'] = x['output'].format(output)
        return x 

    def main_loop(self):
        for i in range(self.lines):
            j = i % self.integers
            k = self.get_from_bag(i, j)
            print(k)

    def get_from_bag(self, line, position):
        print(line + 1, self.bag)
        x = 0
        if position is 0:
            self.bag = [ i for i in range(self.integers) ]
        if len(self.bag) > 0:
            x = random.choice(self.bag)
            self.bag.remove(x)
        return x 


if __name__ == '__main__':
    g = Generate()
    parser = argparse.ArgumentParser(description="One Line", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--name', default='./../../construct-one-line.txt', help='name for "construct" output file.')
    parser.add_argument('--verbose', action="store_true", help="print verbose output.")
    parser.add_argument('--lines', default=100, help='number of examples.')
    parser.add_argument('--prompt', action="store_true", help="output prompt files.")
    parser.add_argument('--integers', default=10, help='highest integers to represent.')

    args = parser.parse_args()
    g.lines = int(args.lines)
    g.verbose = args.verbose
    g.name = args.name
    g.prompt = args.prompt
    g.integers = int(args.integers)

    g.bag = [ i for i in range(g.integers) ]
 
    #g.test_output()
    x = g.substitute_in_json('help', 'me', 'out')
    print(x)
    g.main_loop()
