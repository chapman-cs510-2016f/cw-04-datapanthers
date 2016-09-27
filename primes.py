#!/usr/bin/env python3

import math

"""Module Description
This function takes the input the user puts in, n, and outputs
the factorial of n.
The function will return just the product as an integer.

There are two functions in this script, eratosthenes(n) uses nested while loops to implement the algorithm.
eratosthenes2(n) uses a generator to impelement the algorithm.

"""

def eratosthenes(n):
    """Function Docstring
    eratosthenes(n) -> list
    
    This function will take the number n and return the list of prime numbers less than n in a list. 
    The function does this by first creating a list of all numbers smaller than n into a list. 
    We then implement Eratosthenes' Algorithm by using nested while loops to traverse through the list,
    and removing the numbers that are not prime numbers.
    """
    
    # implementing our initial variables
    i=2
    x= []
    
    # creating a while loop to fill our list with all the numbers smaller than n
    while i<n:
        x.append(i)
        i += 1

    # Nested while loop to traverse through our list, divide the first number of the list with the rest of the numbers
    # and if it is divisible, remove the number from the list. We then increase our counter to find the next prime number
    # and continue until we reach the end of the list.
    counter = 0
    while counter<len(x):
        count2 = counter+1
        while count2<len(x):
            if x[count2]%x[counter] == 0:
                x.remove(x[count2])
            count2 += 1
        counter += 1
        
    return x



def eratosthenes2(n):
    """Function Docstring
    eratosthenes2(n) -> list
    
    This function will use the prime generator function, defined below as gen_eratosthenes()
    to find prime numbers, while this function takes those primes and adds them to our final list.
    We return a list of prime numbers whose values are less than the user input.
    """
    # creating our prime list
    prime_list = []

    # for loop going from 1 to our user input value.
    for i in range(1, n):
        # calling our generator to get the next prime value
        prime = next(p)

        #if the prime number is greater than our initial input value, then we know our list is completed
        # and we exit out of our loop to return our list. Otherwise, we add the prime number to our list.
        if prime > n:
            break
        else:
            prime_list.append(prime)

    return prime_list



def gen_eratosthenes():
    # initiating our initial variable
    count = 2
    
    # our generator loop. Will remain true, until we find a non-prime number
    while True:
        isprime = True

        # As we increase the count, we check the divisors from 2 to square root of n + 1
        # if it is divisible, we break out of the loop as the number is not a prime number.
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        # If the number is a prime, we yield the result, then we increase our counter variable to continue.
        if isprime:
            yield count

        count += 1

p = gen_eratosthenes()


def main(argv):
    print (eratosthenes2(argv))

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print ("Error: did not input a number. Will set a default argument of 5")
        main(5)
    else:
        main(int(argv[1]))
