#!/bin/env python3 

import argparse
import random
import json

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
{}
### Output: {}
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
        self.foreground = 'O'
        self.background = '.'
        self.example = -1

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
            if self.large:
                jk = self.get_large_string(k)
            else:
                jk = [ 'O' for _ in range(k) ]
                jk = '[' + ','.join(jk) + ']'
            # put string in json 
            q = "How many O symbols are inside these brackets?"
            t = jk 
            a = str(k)
            m = ""
            if self.prompt:
                if self.example > -1:
                    ## here we repeat some previous code.
                    a = str(self.example)
                    if self.large:
                        jk = self.get_large_string(self.example)
                    else:
                        jk = [ 'O' for _ in range(self.example) ]
                        jk = '[' + ','.join(jk) + ']'
                    m += self.substitute_in_text(q, jk, a).strip()
                    #m += '\n'
                    pass 
                m += self.substitute_in_text(q, t, '')
                self.list.append([m, k])
            else:
                m = self.substitute_in_json(q, t, a)
                self.list.append(m)
            if self.verbose:
                print(k, i)

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

    def file_loop(self):
        if self.prompt:
            for i in self.list:
                f = open(self.name + '_' + str(i[1]) + '.txt', 'w')
                f.write(i[0].strip())
                f.close()
                pass
        else:
            if self.verbose:
                print('writing -- may take some time...')
            f = open(self.name + '.json', 'w')
            #for i in self.list:
            f.write(json.dumps(self.list) )
            f.close()

    def get_large_string(self, k):
        f = self.foreground
        b = self.background
        j = [ 0 for _ in range(self.integers + 5) ]
        num = 0
        while num < 1000 and j.count(1) < k:
            x = random.randint(0, len(j) - 1)
            j[x] = 1 
            num += 1
        jj = []
        for i in j:
            if i == 1:
                jj.append(f)
            else:
                jj.append(b)
        #jj = [ '0' for i in j if i == 1  ]
        jj = '[' + b.join(jj) + ']'
        if self.verbose:
            print(jj, k)
        return jj 


if __name__ == '__main__':
    g = Generate()
    parser = argparse.ArgumentParser(description="One Line", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--name', default='./../../one-line-dots', help='name and path for "construct" output file.')
    parser.add_argument('--verbose', action="store_true", help="print verbose output.")
    parser.add_argument('--lines', default=100, help='number of examples.')
    parser.add_argument('--prompt', action="store_true", help="output prompt files.")
    parser.add_argument('--integers', default=10, help='highest integers to represent as dots.')
    parser.add_argument('--large_string', action="store_true", help="use large string for containing dots.")
    parser.add_argument('--foreground', default='O', help="set foreground character for large_string.")
    parser.add_argument('--background', default='.', help="set background character for large_string.")
    parser.add_argument('--example', default=-1, help="designate an example to include in prompt output.")

    args = parser.parse_args()
    g.lines = int(args.lines)
    g.verbose = args.verbose
    g.name = args.name
    g.prompt = args.prompt
    g.integers = int(args.integers)
    g.large = args.large_string
    
    g.foreground = args.foreground[0]
    g.background = args.background[0]

    g.example = int(args.example)

    g.bag = [ i for i in range(g.integers) ]

    if g.large:
        g.name += '-large'

    if args.prompt:
        g.lines = 10 
        g.name += '-prompt'
    else:
        g.name += '-train'

    #g.test_output()
    if g.verbose:
        x = g.substitute_in_json('help', 'me', 'out')
        y = g.substitute_in_text('help', 'me', 'out')
        print(x)
        print(y)
        print(g.foreground, g.background, 'characters')
    g.main_loop()
    g.file_loop()
    if g.verbose:
        print(g.list[:10])
