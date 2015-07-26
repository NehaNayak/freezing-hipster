import pickle
import sys
import nltk
from nltk.corpus import wordnet as wn

Lemmas = set()

for synset in list(wn.all_synsets()):
    Lemmas.update(set(synset.lemmas()))

LemmaList = list(map(lambda x:str(x.name()), Lemmas))

TopSenseMap = {}

for lemmaStr in LemmaList:
    synsetList = filter(lambda x :str(x.name().rsplit('.',2)[0])==lemmaStr,wn.synsets(lemmaStr))
    if len(synsetList)>0:
        TopSenseMap[lemmaStr]=synsetList[0].name()

pickle.dump(TopSenseMap,sys.stdout)
