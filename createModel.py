import os
import argparse
import json
from markov import MarkovModel
import pickle

parser = argparse.ArgumentParser(
                    prog='runModel',
                    description='Generate text from a Markov chain model')

parser.add_argument('-p', '--path', help='The directory in which the Discord JSON files reside', default='JSON')
parser.add_argument('-d', '--depth', help='The number of words to use as context for the chain', default=2)
parser.add_argument('-o', '--output', help='The path to write the Markov model to', default='out.markov')
parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
args = parser.parse_args()

model = MarkovModel(args.depth)
    
for directory, _, files in os.walk(args.path):
    for file in files:
        if not file.endswith('.json'):
            continue
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            messages = data['messages']
            for msg in messages:
                text = msg['content']
                if not model.addMessage(text) and args.verbose:
                    print('skipped', text)

model.normalise()
with open(args.output, 'wb') as file:
    pickle.dump(model, file)
print('Successfully created Markov chain model at', args.output)
