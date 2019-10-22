#!/usr/bin/env python
# coding: utf-8


import numpy as np
# If we want to generate walsh code 2 so  power of 2 is 1 
# write order of 2 for e.g 2^3 = 8 for walsh 8\
# walsh code 8 => order 3
# walsh code 16 => order 4
def walsh_code(order):
    #basic element(seed) of walsh code generator
    W = np.array([0])
    for i in range(order):
        W = np.tile(W, (2, 2))
        half = 2**i
        W[half:, half:] = np.logical_not(W[half:, half:])
    return W

print("Walsh code 32 is:",walsh_code(5))






