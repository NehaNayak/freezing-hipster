import sys
import pickle

hypos = pickle.load(open(sys.argv[1],'r'))
hypers = pickle.load(open(sys.argv[2],'r'))

Vocab = set()

for key, values in hypos.iteritems():
    word = key.lower().rsplit('.', 2)[0]
    Vocab.add(word)
    for value in values:
        word = value.lower().rsplit('.', 2)[0]
        Vocab.add(word)

for key, values in hypers.iteritems():
    word = key.lower().rsplit('.', 2)[0]
    Vocab.add(word)
    for value in values:
        word = value.lower().rsplit('.', 2)[0]
        Vocab.add(word)

pickle.dump(sorted(list(Vocab)),sys.stdout)
