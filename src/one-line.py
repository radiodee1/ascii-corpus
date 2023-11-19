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


text_prompt = {
'label': 'three-lines-alpaca',
'slots': 3,
'text': '''

### Instruction:
{}
### Input:
```
{}```
### Output:
{}
'''
}

class Generate:
    def __init__(self):

        self.lines = 0
        self.integers = 10
        self.name = ""
        self.verbose = False
        self.prompt = False
        self.bag = []
        self.large = False
        self.list = []

    def test_output(self):
        print('test_output')

    def substitute_in_json(self, question, statement, output):
        x = json_prompt['text'].copy() 
        x['input'] = x['input'].format(statement)
        x['instruction'] = x['instruction'].format(question)
        x['output'] = x['output'].format(output)
        return x 

    def substitute_in_text(self, question, statement, output):
        x = text_prompt['text']
        x = x.format(str(question), str(statement), str(output))
        return x 

    def main_loop(self):
        for i in range(self.lines):
            j = i % self.integers
            k = self.get_from_bag(i, j)
            # format string 
            jk = [ 'O' for _ in range(k) ]
            jk = '[' + ','.join(jk) + ']'
            # put string in json 
            q = "How many O symbols are inside these brackets?"
            t = jk 
            a = k
            if self.prompt:
                m = self.substitute_in_text(q, t, a)
            else:
                m = self.substitute_in_json(q, t, a)
            self.list.append(m)
            if self.verbose:
                print(k)

    def get_from_bag(self, line, position):
        if self.verbose:
            print(line + 1, self.bag)
        x = 0
        if position == 0:
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
    parser.add_argument('--large_string', action="store_true", help="use large string for containing dots.")

    args = parser.parse_args()
    g.lines = int(args.lines)
    g.verbose = args.verbose
    g.name = args.name
    g.prompt = args.prompt
    g.integers = int(args.integers)
    g.large = args.large_string

    g.bag = [ i for i in range(g.integers) ]

    if args.prompt:
        g.lines = 10 

    #g.test_output()
    if g.verbose:
        x = g.substitute_in_json('help', 'me', 'out')
        y = g.substitute_in_text('help', 'me', 'out')
        print(x)
        print(y)
    g.main_loop()

    print(g.list)
