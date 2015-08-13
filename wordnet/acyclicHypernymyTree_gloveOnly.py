import sys
import pickle
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

def main():

    glovemus = pickle.load(open(sys.argv[1],'r'))

    Hyponyms = {}
    
    for syn in list(wn.all_synsets()):
        hyponyms = syn.hyponyms()
        if len(hyponyms)>0:
            Hyponyms[syn.name()]= map(lambda x: x.name(), hyponyms)
    
    top = set(Hyponyms.keys()) - set([word for hypos in Hyponyms.values() for word in hypos])
    
    Hyponyms["1"] = list(top)
    Stack = ["1"]
    Vocab = set()
    
    acyclicPairs = []
    
    while len(Stack)>0:
        node = Stack.pop(-1)
        if node[0] not in Vocab:
            Vocab.add(node[0])
            if node!='1':
                acyclicPairs.append(node)
            if node[0] in Hyponyms.keys():
                for hypo in Hyponyms[node[0]]:
                    Stack.append((hypo,node[0]))

    #print "made acyclic pairs"

    actualHyponyms = defaultdict(list)

    Hypernyms = {}
    
    for pair in acyclicPairs:
        (hypo, hyper) = pair
        actualHyponyms[hyper].append(hypo)
        Hypernyms[hypo] = hyper

        print pair

    #print "made actual hyponyms and hypernyms"

    #pickle.dump((actualHyponyms,Hypernyms), sys.stdout)

    """
    Queue = ["1"]
    VisitOrder = []

    while len(Queue)>0:
        top = Queue.pop(0)
        VisitOrder.append(top)
        for hypo in actualHyponyms[top]:
            Queue.append(hypo)

    VisitOrder = list(reversed(VisitOrder))[1:]

    #print len(VisitOrder)
    #nonRoots = [nr for hypos in actualHyponyms.values() for nr in hypos]
    #print len(nonRoots)
    #print len(set(nonRoots))
    #print len(set(actualHyponyms.keys()).union(set(nonRoots)))

    #print VisitOrder[:10]
    #print VisitOrder[-10:]

    for node in VisitOrder:
        if 'aminobutyric' in node:
            print "found it", node
        word = node.lower().rsplit('.', 2)[0]
        if word not in glovemus and not node=='1':
            if node in Hyponyms:
                actualHyponyms[Hypernyms[node]].extend(actualHyponyms[node])
            actualHyponyms[Hypernyms[node]].remove(node)
            print "#" , word
        else:
            print "$", word
            pass

    for key, values in actualHyponyms.iteritems():
        print key, values    
         
    #pickle.dump(actualHyponyms, sys.stdout)
    """
        
if __name__=="__main__":
    main()
