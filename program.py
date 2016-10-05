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
    for i in range(len(overlist)):
        if i != 








    pl.figure()
    pl.hist(delta_circumsized, normed=1, bins=100, label="Histogram")
    
    prob = P(delta_circumsized, Sc)
    pl.plot(delta_circumsized, prob, '.', label="Analytical")
    pl.legend(loc='best')
    pl.title("Exercise 2.5")














if __name__ == '__main__':
    run()

    # another_run()
    pl.show()