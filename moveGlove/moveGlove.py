import sys
import pickle
import numpy as np

def normalize(vec):
    return vec/np.linalg.norm(vec)

def moveNode(node, offset):
    mus[node]+=offset
    if node in hyponymMap.keys():
        for hypo in hyponymMap[node]:
            moveNode(hypo, offset)

def main():
    # load things
    hyponymMap = pickle.load(open(sys.argv[1],'r'))
    glovemus = pickle.load(open(sys.argv[2],'r'))
    mus = {}

    # traversal things
    toVisit = [1]
    visitOrder = [] # gets non-leaf nodes in BFS order
    keys = set(hyponymMap.keys())
    values = set(sum(hyponymMap.values(),[]))
    top = keys - values
    hyponymMap[1] = []
    for topWord in top:
        hyponymMap[1].append(topWord)      
    while len(toVisit)>0:
        node = toVisit.pop(0)
        if not node == 1 :
            lem = node.lower().rsplit('.', 2)[0]
            mus[node] = glovemus[lem]

        if node in hyponymMap.keys():
            visitOrder.append(node)
            for hyponym in hyponymMap[node]:
                toVisit.append(hyponym)

    visitOrder = list(reversed(visitOrder))[:-1] # remove dummy top node

    learningRate = 0.0001
    learningRate2 = 0.0001
    """
    for node in visitOrder[:10]:
        print mus[node]

    for node in visitOrder:
        hypos = hyponymMap[node]
        median = sum(map(lambda x:mus[x], hypos))/len(hypos)
        for hypo in hypos:
            diff = np.zeros(np.size(mus[hypo]))
            for hypo2 in hypos:
                if not hypo == hypo2:
                    diff -=learningRate*(mus[hypo]-mus[hypo2])
            mus[hypo]+=diff
            mus[hypo]=normalize(mus[hypo])
        mus[node]-= learningRate2*(mus[node]-median)
        mus[node]=normalize(mus[node])
          
    
    for node in visitOrder[:10]:
        print mus[node]
    """
    for node in visitOrder:
        for hypo in hyponymMap[node]:
            if hypo in hyponymMap.keys():
                break
            for hypo2 in hyponymMap[node]:
                print np.linalg.norm(mus[hypo]-mus[hypo2])
        
if __name__=="__main__":
    main()
