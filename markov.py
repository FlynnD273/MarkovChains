import numpy as np
import re

class MarkovModel:
    def __init__(self, contextLength: int) -> None:
        self.contextLength = contextLength
        self.ctxmap = {}
        self.__isNormalised = False

    def addMessage(self, msg: str) -> bool:
        # msg = str.lower(msg)
        if msg.startswith("https://"):
            return False
        # msg = re.sub("[^A-Za-z ]", "", msg)
        if len(msg) < self.contextLength or self.__isNormalised:
            return False

        tokens = msg.split()
        for i in range(self.contextLength, len(tokens) - 1):
            self.addEntry(" ".join(tokens[i - self.contextLength:i]), tokens[i])
        self.addEntry(" ".join(tokens[-self.contextLength:]), None)

        return True

    def addEntry(self, context: str, word: str | None) -> bool:
        if self.__isNormalised:
            return False

        if self.ctxmap.get(context) is None:
            self.ctxmap[context] = {}
        if self.ctxmap[context].get(word) is None:
            self.ctxmap[context][word] = 0

        self.ctxmap[context][word] += 1

        return True

    def normalise(self) -> None:
        for ctx in self.ctxmap.keys():
            total = float(sum(self.ctxmap[ctx].values()))
            for char in self.ctxmap[ctx]:
                self.ctxmap[ctx][char] /= total
        self.__isNormalised = True
    
    def getNext(self, ctx: str) -> str | None:
        if self.ctxmap.get(ctx) is None:
            return " "

        chars = list(self.ctxmap[ctx].keys())
        vals = list(self.ctxmap[ctx].values())
        return np.random.choice(chars, p=vals)

    def generate(self, start: str, maxCount: int) -> str:
        words = start.split()
        if len(words) < self.contextLength:
            return start
        if not self.__isNormalised:
            return ""

        count = 0
        while count < maxCount:
            ctx = " ".join(words[-self.contextLength:])
            next = self.getNext(ctx)
            if next is None:
                break;
            words.append(next)
            count += 1

        return " ".join(words)


