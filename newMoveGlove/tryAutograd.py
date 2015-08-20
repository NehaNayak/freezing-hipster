from __future__ import absolute_import
from __future__ import print_function
import autograd.numpy as np
import autograd.numpy.random as npr
#from autograd import grad
from autograd import value_and_grad
from autograd.util import quick_grad_check
#from scipy.optimize import minimize
#from six.moves import range

class WeightsParser(object):
    """A helper class to index into a parameter vector."""
    def __init__(self):
        self.idxs_and_shapes = {}
        self.num_weights = 0

    def add_shape(self, name, shape):
        start = self.num_weights
        self.num_weights += np.prod(shape)
        self.idxs_and_shapes[name] = (slice(start, self.num_weights), shape)

    def get(self, vect, name):
        idxs, shape = self.idxs_and_shapes[name]
        return np.reshape(vect[idxs], shape)

    def stack(self, datum):
        weights = np.zeros(self.num_weights)
        for key, value in datum.iteritems():
            weights[self.idxs_and_shapes[key][0]]=value        
        return weights

def KLD(vector_size):
    parser = WeightsParser()
    parser.add_shape('mu1', (1, vector_size))
    parser.add_shape('mu2', (1, vector_size))
    parser.add_shape('sig1', (1, 1))
    parser.add_shape('sig2', (1, 1))

    def loss(weights):
        mu1 = parser.get(weights, 'mu1')
        mu2 = parser.get(weights, 'mu2')
        sig1 = parser.get(weights, 'sig1')*np.eye(mu1.size)
        sig2 = parser.get(weights, 'sig2')*np.eye(mu1.size)

        
        return 0.5*( \
            np.log(np.linalg.det(sig2) / np.linalg.det(sig1)) \
            - mu1.size \
            + np.trace(np.dot(np.linalg.inv(sig2),sig1)) \
            #+ np.dot(np.dot(np.transpose(mu2 - mu1), np.linalg.inv(sig2)), mu2 - mu1 )
            + np.dot(np.dot(mu2 - mu1, np.linalg.inv(sig2)), np.transpose(mu2 - mu1 ))
            )
    
    return parser, loss

def pairwise_distance(vector, size):

    print np.split(vector)
        
    def stack(vectors):
   
    def loss(): 
        
        sum = 0.0
        for i, vectori in enumerate(vectors):
            for j in range(i):
                sum+=np.linalg.norm(vectori,vectors[j])
    return sum
    
def main():
    (parser, loss) = KLD(50)
    print(parser)
    print(parser.idxs_and_shapes)
    datum = {}
    datum['mu1']=np.zeros(50)
    datum['mu2']=np.ones(50)
    datum['sig1']=5
    datum['sig2']=6

    trial_vecs = []
    for _ in range(5):
        trial_vecs.append(np.random.rand(50))
    value_and_grad_fun = value_and_grad(pairwise_distance)
    value, grad = value_and_grad_fun(trial_vecs)
    

    print(trial_vecs)

    weights = parser.stack(datum)
    value_and_grad_fun = value_and_grad(loss)
    value, grad = value_and_grad_fun(weights)
    print(value)
    weights = weights - 10e-4*grad
    value, grad = value_and_grad_fun(weights)
    print(value)


    pass 

if __name__ == "__main__":
    main()
