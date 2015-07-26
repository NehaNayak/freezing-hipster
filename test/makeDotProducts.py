import sys
import pickle
from numpy import *
from collections import defaultdict
from hipster_utils import *

Distributions = pickle.load(open(sys.argv[1],'r'))
DistributionKeys = defaultdict(list)

for key in Distributions.keys():
    lemma, pos, synset_index_str = key.lower().rsplit('.', 2)
    DistributionKeys[lemma].append(key)

#print DistributionKeys

WordPairs = []

for line in sys.stdin:
    (word1, word2, values) = line.split()
    WordPairs.append((word1, word2))

#print WordPairs

for word1, word2 in WordPairs:
    maxDotProduct = 0.0
    wordList1 = DistributionKeys[word1]
    wordList2 = DistributionKeys[word2]
    for syn1 in wordList1:
        for syn2 in wordList2:
            dotP = dotProduct(Distributions[syn1], Distributions[syn2])
            #print syn1, syn2, dotP
            if dotP > maxDotProduct:
                maxDotProduct = dotP

    print word1, word2, maxDotProduct

    
