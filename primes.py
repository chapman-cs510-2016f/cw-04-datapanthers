#!/usr/bin/env python3

import math

"""CS510 - Classwork 4 - Prime Numbers
This module is uses to takes an integer input, n, and outputs a list of strings giving 

There are two functions in this script:
    eratosthenes(n) uses nested while loops to implement the algorithm.
    eratosthenes2(n) uses a generator to implement the algorithm.
When calling the module on an interpreter, the module will pass the initial value, n, through the function
eratosthenes2(n).

Inside the generator function, we took inspiration from this site about producing a generator for prime numbers.
http://codereview.stackexchange.com/questions/74550/prime-number-sequence-generator

"""

def eratosthenes(n):
    """Eratosthenes Algorithm
    eratosthenes(n) -> list
    
    This function will take the number n and return the list of prime numbers less than n in a list. 
    The function does this by first creating a list of all numbers smaller than n into a list. 
    We then implement Eratosthenes' Algorithm by using nested while loops to traverse through the list,
    and removing the numbers that are not prime numbers.
    """
    
    # implementing our initial variables
    counter = 2
    final_list= []
    
    # creating a while loop to fill our list with all the numbers smaller than n
    while counter < n:
        final_list.append(counter)
        counter += 1
    #
    ### INSTRUCTOR COMMENT:
    # Above is a cumbersome way to create a list of consecutive integers (though it works).
    # Consider range(n), which does this automatically.
    # Or, if you need to create a nontrivial list, consider a list comprehension.
    #

    # Nested while loop to traverse through our list, divide the first number of the list 
    # with the rest of the numbers and if it is divisible, remove the number from the list.
    # We then increase our counter to find the next prime number and continue until we reach the end of the list.
    counter = 0
    while counter < len(final_list):
        count2 = counter + 1
        while count2<len(final_list):
            if final_list[count2] % final_list[counter] == 0:
                final_list.remove(final_list[count2])
            count2 += 1
        counter += 1
        
    return final_list



def eratosthenes2(n):
    """Eratosthenes Algorithm, version two
    eratosthenes2(n) -> list
    
    This function will use the prime generator function, defined below as gen_eratosthenes()
    to find prime numbers, while this function takes those primes and adds them to our final list.
    We return a list of prime numbers whose values are less than the user input.
    """
    p = gen_eratosthenes()
    
    # creating our prime list
    prime_list = []

    # We produce a while loop that will call our generator infinitely amount of times, 
    # appending our prime number and exiting when needed.
    while True:
        # calling our generator to get the next prime value
        prime = next(p)

        # This if statement ensures that we exit out of the loop once the generator produces a
        # prime number, larger than our n. Otherwise it adds the prime number to our list.
        if prime >= n:
            break
        else:
            prime_list.append(prime)
    
    #
    ### INSTRUCTOR COMMENT:
    # The above logic is very convoluted.  Typically, if you have to invoke "break", then you
    # should rethink your algorithm to see if there is a simpler way to do what you are trying
    # to do. In this case, you can replace this entire function block by a list comprehension:
    #   return [next(p) for _ in range(n)]

    return prime_list



def gen_eratosthenes():
    """Erastosthenes generator funtion

    This function uses a generator to calculate the next prime number and yields the result.
    It does so by using a for loop, with I gained inspiration from the website, sourced in the module docstring,
    """
    # initiating our initial variable as 2, as it is the first prime number (We are not considering 1 to be prime)
    count = 2

    # We create a while loop that can run infinitely amount of times.
    while True:
        prime = True

        # This equation inside the for loop, which I have cited above in my module docstring,
        # will always produce numbers low enough to check our count variable by taking the square root of 
        # the count, then adding one.
        # If the loop will then use the the modulo of our count varible and will only yield count
        # if it is non divisible by any other number that is checked within the for statement.
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                prime = False
                break

        if prime:
            yield count

        count += 1





def main(fact):
    print (eratosthenes2(fact))

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print ("Error: did not input a number. Will set a default argument of 5")
        main(5)
    else:
        try:
            val = int(argv[1])
            if int(argv[1]) < 0:
                print ("Error: inputed a negative number. Please enter a positive number")
            elif int(argv[1]) == 0:
                print ("Error: inputed 0, Please enter a number greater than 1")
            else:
                main(int(argv[1]))
        except ValueError:
            print("Input was not an integer!")
