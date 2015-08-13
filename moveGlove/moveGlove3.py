import numpy as np
import sys
import pickle

def distanceSum(hyponyms):
    distSum = 0.0
    for vec1 in hyponyms:
        for vec2 in hyponyms:
            distSum += np.linalg.norm(vec1[0]-vec2[0])
    return distSum
        

# get wordnet tree
Hyponyms = dict(pickle.load(open(sys.argv[1],'r')))

# get glove vectors
gloveVectors = dict(pickle.load(open(sys.argv[2],'r')))

newVectors = pickle.load(open('moveGlove2.pickle','r'))

#print list(sum(Hyponyms.values(),[]))
tops = set(Hyponyms.keys())-set(list(sum(Hyponyms.values(),[])))

Queue = list(tops)
VisitOrder = []

while len(Queue)>0:
    top = Queue.pop(0)
    VisitOrder.append(top)
    if top in Hyponyms:
        Queue+=Hyponyms[top]

learningRate = 0.01

for i in range(1):
    for top in VisitOrder:
        if top in Hyponyms:
            hypoVecs = [newVectors[hypo] for hypo in Hyponyms[top]]
            centroid = np.sum([hypoVec[0] for hypoVec in hypoVecs])/len(hypoVecs)
            print distanceSum(hypoVecs)
            for hypo in Hyponyms[top]:
                newVectors[hypo] = list(newVectors[hypo])
                newVectors[hypo][0] -=learningRate*(newVectors[hypo][0]-centroid)
                norm = np.linalg.norm(newVectors[hypo][0])
                if norm> 0:
                    newVectors[hypo][0] /=newVectors[hypo][0]/norm
                print distanceSum(hypoVecs)
            Queue+=Hyponyms[top]
        print len(Queue)
    dsds
    for top in list(reversed(VisitOrder)):
        if top in Hyponyms and top != '1':
            print top, Hyponyms[top]
            print [np.linalg.norm(newVectors[top][0] - hypo[0]) for hypo in [newVectors[x] for x in Hyponyms[top]] ]
            maxDist = max([np.linalg.norm(newVectors[top][0] - hypo[0]) for hypo in [newVectors[x] for x in Hyponyms[top]] ])
            maxVar = max([hypo[1] for hypo in [newVectors[x] for x in Hyponyms[top]]])
            if top[1] > maxVar+maxDist:
                print top[1], maxVar, maxDist
            else:
                print "boo"
             
