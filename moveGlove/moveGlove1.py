import numpy as np
import sys
import pickle

# get wordnet tree
Hyponyms = pickle.load(open(sys.argv[1],'r'))

# get glove vectors
gloveVectors = pickle.load(open(sys.argv[2],'r'))

del Hyponyms['black_buffalo.n.01']
Hyponyms['sucker.n.07'].pop(-1)

newVectors = {}

# find visitOrder
Queue = ["1"]
VisitOrder = []

while len(Queue)>0:
    top = Queue.pop(0)
    VisitOrder.append(top)
    for hypo in Hyponyms[top]:
        Queue.append(hypo)

VisitOrder = list(reversed(VisitOrder))[:-1]

leafVariance = 0.06

# go over and assign variances
for node in VisitOrder:
    if node in Hyponyms.keys() and len(Hyponyms[node])>0:
        word = node.lower().rsplit('.', 2)[0]
        newMu = gloveVectors[word]
        hypMus = [newVectors[hypo][0] for hypo in Hyponyms[node]]
        var = max([np.linalg.norm(newMu-hypMu) for hypMu in hypMus])
        newVectors[node] = (gloveVectors[word],var)
    else:
        word = node.lower().rsplit('.', 2)[0]
        newVectors[node] = (gloveVectors[word],leafVariance)

Lemmas = set([node.lower().rsplit('.', 2)[0] for node in Hyponyms.keys()])
otherLemmas = set([node.lower().rsplit('.', 2)[0] for node in list(sum(Hyponyms.values(),[]))])

Lemmas = Lemmas.union(otherLemmas)

pickle.dump(newVectors.keys(),sys.stdout)   
