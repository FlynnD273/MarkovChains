import os
import json
from markov import MarkovModel

dataDirectory = "JSON"

model = MarkovModel(2)

for directory, _, files in os.walk(dataDirectory):
    for file in files:
        with open(os.path.join(directory, file), "r", encoding="utf-8") as fp:
            data = json.load(fp)
            messages = data["messages"]
            for msg in messages:
                text = msg["content"]
                if not model.addMessage(text):
                    # print("skipped", text)
                    _ = None

model.normalise()
print(model.generate("so apparently", 50))
