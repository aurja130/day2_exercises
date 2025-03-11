#!/usr/bin/python

import numpy as np
from math import sqrt
import time

def gen_primes(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n"""
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = False
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
    return np.ndarray.tolist(np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)])

@profile
def factorize(n,primes):
    factors = []
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors.append(p)
        if(p > sqrt(n)):
            break
    if(n > 1):
        factors.append(n)
    return factors

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
        else:
            phi *= (factors[i]-1)
    return phi

@profile
def runner(m):
    primes = gen_primes(m)
    fraq = 0
    for i in range(2,m+1):
        fraq += fast_phi(i,primes)
    
    print(fraq)

start = time.time()
runner(1000000)
print(f'Time: {time.time()-start} seconds.')