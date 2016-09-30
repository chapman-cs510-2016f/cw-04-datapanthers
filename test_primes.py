#!/usr/bin/env python3

import primes

def test_primes():
    testTheResults=[2,3,5,7]
    result = primes.eratosthenes(10)
    assert testTheResults==result
    
    testTheResults=[2,3,5]
    result = primes.eratosthenes(7)
    assert testTheResults==result
    
    
    testTheResults=[2, 3, 5, 7, 11, 13, 17, 19]
    result = primes.eratosthenes(20)
    assert testTheResults==result
    