import pylab as pl
import numpy as np

def Sc(k):
    return 2*pl.pi/float(k)

def sigma(Sc):
    return pl.pi/float(Sc**4)

def P(delta, Sc):
    return pl.exp( -(delta**2)/(2.*sigma(Sc)**2) )/(sigma(Sc)*(2*pl.pi)**0.5)

def run():
    N = int(1e5)

    epsilon = 0.99
    Sc = 2*(10*(pl.pi**0.25))
    sigma_init = sigma(Sc)
    delta = np.random.normal(loc=0.0, scale=sigma_init, size=N)
    overlist = []

    while Sc > 1.0:
        Sc_new = Sc*epsilon
        sigma_new = (sigma(Sc_new)**2 - sigma(Sc)**2)**0.5
        Beta = np.random.normal(loc=0.0, scale=sigma_new, size=N)
        delta += Beta
        for k in range(len(delta)):
            if delta[k] > 1.0:
                overlist.append(k)

        Sc = Sc_new
    
    pl.figure()
    pl.hist(delta, normed=1, bins=100, label="Histogram")
        
    prob = P(delta, Sc)
    pl.plot(delta, prob, '.', label="Analytical")
    pl.legend(loc='best')
    pl.title("Exercise 2.4")

    ####

    delta_mod = []
    for i in range(len(delta)):
        for j in overlist:
            if i != j:
                delta_mod.append(delta[i])

    pl.figure()
    pl.hist(delta_mod, normed=1, bins=100, label="Histogram")
    
    prob = P(delta_mod, Sc)
    pl.plot(delta_mod, prob, '.', label="Analytical")
    pl.legend(loc='best')
    pl.title("Exercise 2.5")



if __name__ == '__main__':
    run()
    pl.show()