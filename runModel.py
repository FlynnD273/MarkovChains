import pickle
import argparse
from markov import MarkovModel

parser = argparse.ArgumentParser(
                    prog='runModel',
                    description='Generate text from a Markov chain model')

parser.add_argument('start', help='The starting prompt for generation')
parser.add_argument('-p', '--path', help='The path to the Markov pickle file', default='out.markov')
parser.add_argument('-c', '--count', help='Maximum number of words to generate', default=50)

args = parser.parse_args()
model: MarkovModel = MarkovModel(0)

with open(args.path, "rb") as file:
    model = pickle.load(file)

print(model.generate(args.start, args.count))
