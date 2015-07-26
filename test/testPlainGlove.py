import numpy as np
import sys
import pickle

WordList = []

WordPairList = sys.stdin

for line in WordPairList:
    (word1, word2, rating) = line.split()
    WordList.append((word1, word2))

Vectors = pickle.load(open(sys.argv[1],'r'))

for word1, word2 in WordList:
    vec1 = Vectors[word1]
    vec2 = Vectors[word2]
    similarity = vec1.dot(vec2)
    sys.stdout.write(word1+"\t"+word2+"\t"+str(similarity))
