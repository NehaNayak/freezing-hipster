import numpy as np
import sys
import pickle

Hyponyms = pickle.load(open(sys.argv[1],'r'))
GloveMus = pickle.load(open(sys.argv[2],'r'))

for hyper, hypos in Hyponyms.iteritems():
    try:
        for hypo1 in hypos:
            vec1 = GloveMus[hypo1.lower().rsplit('.', 2)[0]]
            for hypo2 in hypos:
                vec2 = GloveMus[hypo2.lower().rsplit('.', 2)[0]]
                print np.linalg.norm(vec1 - vec2)
    except KeyError:
        pass
