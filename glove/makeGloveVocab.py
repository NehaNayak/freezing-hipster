import sys
import pickle

Vocab = set()

for line in sys.stdin:
    Vocab.add(line[:-1])

pickle.dump(Vocab, sys.stdout)
