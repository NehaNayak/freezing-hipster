import sys
import pickle
import nltk
from nltk.corpus import wordnet as wn
from collections import defaultdict

def main():
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

    actualHyponyms = defaultdict(list)

    for pair in acyclicPairs:
        (hypo, hyper) = pair
        actualHyponyms[hyper].append(hypo)


    print actualHyponyms["1"]

    dsds
    pickle.dump(actualHyponyms, sys.stdout)
        
if __name__=="__main__":
    main()
