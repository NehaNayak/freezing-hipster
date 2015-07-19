import sys
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict
import pickle

gloveLemmas = pickle.load(open(sys.argv[1],'r'))

hyperPickleFile = open(sys.argv[2]+"_hypernyms.pickle",'w')
hypoPickleFile = open(sys.argv[2]+"_hyponyms.pickle",'w')

Hypernyms = defaultdict(list)
Hyponyms = defaultdict(list)

for syn in list(wn.all_synsets()):
    synlem = syn.name().lower().rsplit('.', 2)[0]
    if synlem in gloveLemmas:
        for hyp in syn.hypernyms():
            hyplem = hyp.name().lower().rsplit('.', 2)[0]
            if hyplem in gloveLemmas:
                Hypernyms[syn.name()].append(hyp.name())
                Hyponyms[hyp.name()].append(syn.name())

pickle.dump(Hypernyms, hyperPickleFile) 
pickle.dump(Hyponyms, hypoPickleFile) 
