import sys
import pickle
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

def main():

    glovemus = pickle.load(open(sys.argv[1],'r'))

    (actualHyponyms, Hypernyms) = pickle.load(open(sys.argv[2],'r'))    

    Queue = ["1"]
    VisitOrder = []

    while len(Queue)>0:
        top = Queue.pop(0)
        VisitOrder.append(top)
        for hypo in actualHyponyms[top]:
            Queue.append(hypo)

    VisitOrder = list(reversed(VisitOrder))[1:]

    for node in VisitOrder:
        word = node.lower().rsplit('.', 2)[0]
        if word not in glovemus and not node=='1':
            if node in actualHyponyms:
                actualHyponyms[Hypernyms[node]].extend(actualHyponyms[node])
            actualHyponyms[Hypernyms[node]].remove(node)
            del actualHyponyms[node]
        else:
            pass

    for i in actualHyponyms.values():
        print len(i)
    #pickle.dump(actualHyponyms, sys.stdout)
        
if __name__=="__main__":
    main()
