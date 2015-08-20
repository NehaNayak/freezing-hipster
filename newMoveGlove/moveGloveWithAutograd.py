from __future__ import division
import pickle
import sys
import numpy as np

def synset_to_lemma(synset):
    return synset.rsplit('.')[0]

def centroid(vec_list):
    mu = np.sum(vec_list, axis=0)/len(vec_list)
    return mu

def assign_wordnet_vectors(wordnet_tree, glove_vectors, min_variance):
   
    wordnet_vectors = {}
 
    for node in visit_order:

        mu = None
        sig = None

        # find the lemma
        lemma = synset_to_lemma(node)

        if lemma in glove_vectors.keys():
            # retrieve the glove vector
            mu = glove_vectors[lemma]

        # if no lemma
        elif len(wordnet_tree[node]) > 0:
            # get the centroid of hypernyms
            mu = centroid([wordnet_vectors[hypo][0] for hypo in wordnet_tree[node]])

        # if no lemma and no hypernyms
        else:
            # get fake lemma
            fake_lemma = lemma.split('_')[-1]
            # retrieve the glove vector
            if fake_lemma in glove_vectors.keys():
                mu = glove_vectors[fake_lemma]
            else:
                mu = np.zeros(50)
   

        # if leaf
        if len(wordnet_tree[node]) == 0:
            # min_variance
            sig = min_variance
        # otherwise
        else:
            # get max distance
            sig = max([

                np.linalg.norm(mu - wordnet_vectors[hypo][0])+wordnet_vectors[hypo][1]

                for hypo in wordnet_tree[node]])

        wordnet_vectors[node] = [mu, sig] 

    return wordnet_vectors
    

def find_visit_order(tree):
    queue = ["1"]
    visit_order = []
    while len(queue) > 0:
        top = queue.pop(0)
        visit_order.append(top)
        queue += tree[top]
    return list(reversed(visit_order))

def main():

    # read in Wordnet tree
    
    wordnet_tree = pickle.load(open(sys.argv[1],'r'))
    global visit_order
    visit_order = find_visit_order(wordnet_tree)
    
    # read in GloVe vectors

    glove_vectors = pickle.load(open(sys.argv[2],'r'))
    
    # start at leaves and assign vectors and variances

    min_variance = 0.06
    wordnet_vectors = assign_wordnet_vectors(wordnet_tree, glove_vectors, min_variance) 

    # dump

    pickle.dump(wordnet_vectors, sys.stdout)
    
    # start at leaves and contract with 
    
    # start at root (?) and reassign variances
    

if __name__ == "__main__":
    main()
