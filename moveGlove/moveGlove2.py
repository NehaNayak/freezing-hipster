import numpy as np
import sys
import pickle

# get wordnet tree
Hyponyms = dict(pickle.load(open(sys.argv[1],'r')))

# get glove vectors
gloveVectors = dict(pickle.load(open(sys.argv[2],'r')))

newVectors = {}

# find visitOrder
Queue = ["1"]
VisitOrder = []

while len(Queue)>0:
    top = Queue.pop(0)
    VisitOrder.append(top)
    if top in Hyponyms:
        for hypo in Hyponyms[top]:
            Queue.append(hypo)

VisitOrder = list(reversed(VisitOrder))[:-1]


leafVariance = 0.06

# go over and assign variances
for node in VisitOrder:

    if node in Hyponyms.keys() and len(Hyponyms[node])>0: # nonleaf

        word = node.lower().rsplit('.', 2)[0]

        if word not in gloveVectors.keys(): # mwe
            hypMus = [newVectors[hypo][0] for hypo in Hyponyms[node]]
            hypVars = [newVectors[hypo][1] for hypo in Hyponyms[node]]
            nodeMu = np.sum(hypMus,axis=0)/len(hypMus)
            muNorm = np.linalg.norm(nodeMu)
            if muNorm > 0:
                nodeMu = nodeMu/muNorm
            nodeDistances = [np.linalg.norm(hypMu - nodeMu) for hypMu in hypMus]
            newVectors[node] = (nodeMu,max(nodeDistances)+max(hypVars))
            
        else: # swe
            newVectors[node] = (gloveVectors[word],leafVariance)

    else: # non-nonleaf

        word = node.lower().rsplit('.', 2)[0]
        if word in gloveVectors.keys():
            newVectors[node] = (gloveVectors[word],leafVariance)
        else:
            subWord = word.split("_")[-1]
            if subWord in gloveVectors:
                newVectors[node] = (gloveVectors[subWord],leafVariance)
            else:
                newVectors[node] = (np.zeros(gloveVectors[gloveVectors.keys()[0]].size),leafVariance)
            
pickle.dump(newVectors,sys.stdout)   
