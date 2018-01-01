#Generating the Stanislaw Ulam's prime spiral
#It is a spiral-like layout of integers on a 2D plane
#where prime integer cells are filled
#and when plotted, visible straight lines appear.
#That demonstrates that (quite surprisingly) certain parabolas contain more primes than others
#https://en.wikipedia.org/wiki/Ulam_spiral

import numpy as np
import matplotlib.pyplot as plt

#computes prime numbers up to max using Sieve of Eratosthenes
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def getPrimes(max):
    available = np.array([True for i in range(0,max)],dtype = np.int64)
    for d in range(2,max):
        if available[d]:
            maxmul = int(np.ceil((max)/d)) #maximal multiplicative factor for d to reach up to max
            inds = [int(d*m) for m in range(2,maxmul+1) if int(d*m)<max]
            available[inds] = False
    return [i for i in range(1,max) if available[i]]

P = getPrimes(100*100)
#print(P)

#generating the spiral as a numpy array
#a cell is the number if prime, otherwise 0
def generateSpiral(halfsize = 10):

    N = (2*(halfsize-1)+1)**2
    A = 2*halfsize+1

    primes = getPrimes(N)

    M = np.zeros((A,A)) #taken positions
    U = np.zeros((A,A)) #Ulam spiral

    #position of 2
    x = halfsize+1
    y = halfsize
    M[y,x] = 1
    U[y,x] = 2

    #position of 1
    M[y,x-1] = 1
    U[y,x-1] = 1

    #stepping through the square spiral
    for i in range(3,N):

        if (M[y+1,x] == 0) and (M[y,x-1] == 1):
            y = y + 1
            M[y,x] = 1
            U[y,x] = (i in primes)*i
        elif (M[y,x-1] == 0) and (M[y-1,x] == 1):
            x = x - 1
            M[y,x] = 1
            U[y,x] = (i in primes)*i
        elif (M[y-1,x] == 0) and (M[y,x+1] == 1):
            y = y - 1
            M[y,x] = 1
            U[y,x] = (i in primes)*i
        else:
            x = x + 1
            M[y,x] = 1
            U[y,x] = (i in primes)*i

        #print(U)

    return U

#########

#testing for 50x50 plot
R = 50
M = (generateSpiral(R) > 0).astype(int)
plt.title('Ulam spiral up to '+str((2*(R-1)+1)**2), fontsize=22)
plt.axis('off')
plt.axis('equal')
plt.imshow(-1.0*M,cmap="hot",interpolation="nearest")
plt.show()

#########

mass_produce = True
radii = [10,20,30,40,50] #radii to go through

if mass_produce: #generating a succession of gradually growing Ulam spirals
    #mass production
    for R in radii:

        M = (generateSpiral(R) > 0).astype(int)

        plt.title('Ulam spiral up to '+str((2*(R-1)+1)**2), fontsize=22)
        plt.axis('off')
        plt.axis('equal')
        plt.imshow(-1.0*M, cmap="hot", interpolation='nearest')
        plt.savefig("ulams_prime_spiral_"+str((2*(R-1)+1)**2)+".png", bbox_inches=None, pad_inches=0.1)
        print("done",R)
