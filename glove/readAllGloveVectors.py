import sys
from numpy import *
import pickle

def main():
    
    Vectors = {}

    for line in sys.stdin:
        thisLine = line.split()
        try:
            vec = asarray(map(lambda x: float(x),thisLine[1:]))
            Vectors[word] = vec/linalg.norm(vec)

    pickle.dump(Vectors, sys.stdout)

if __name__=="__main__":
    main()
