#!/usr/bin/env python3

import primes

def test_primes():
    testTheResults=[2,3,5,7]
    result = primes.eratosthenes(10)
    assert testTheResults==result
    print("it works. iam here")
    