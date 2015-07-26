import sys
from numpy import *
import pickle

def main():
    wordnetVocab = pickle.load(open(sys.argv[1],'r'))

    Vectors = {}

    for line in sys.stdin:
        thisLine = line.split()
        try:
            word = unicode(thisLine[0])
            if word in wordnetVocab:
                vec = asarray(map(lambda x: float(x),thisLine[1:]))
                Vectors[word] = vec/linalg.norm(vec)
        except UnicodeDecodeError:
            pass

    pickle.dump(Vectors, sys.stdout)

if __name__=="__main__":
    main()
