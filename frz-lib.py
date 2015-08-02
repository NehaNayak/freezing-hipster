import numpy as np

def KLD(mu1, mu2, sig1, sig2):
    n = mu1.size
    Sig1 = sig1*np.eye(n)
    Sig2 = sig2*np.eye(n)
    muDiff = mu2 - mu1

    return 0.5*(
        np.log(np.linalg.det(Sig2)/np.linalg.det(Sig1))
        - n
        + np.trace(np.linalg.inv(Sig2).dot(Sig1))
        + (muDiff.T).dot(np.linalg.inv(Sig2)).dot(muDiff)
    )

def main():
    mu1 = np.zeros(5)
    mu2 = np.zeros(5)
    mu1[0] = 1.0
    mu2[0] = 1.1
    print KLD(mu1, mu2, 0.5, 0.05)
    print KLD(mu1, mu2, 0.05, 0.5)

if __name__=="__main__":
    main()
