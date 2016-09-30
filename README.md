# CS510 CW 4

**Author(s):** _Simrath Ratra, Afnan Alqahtani, Andrew nguyen_

[![Build Status](https://travis-ci.org/chapman-cs510-2016f/cw-04-datapanthers.svg?branch=master)](https://travis-ci.org/chapman-cs510-2016f/cw-04-datapanthers)

**Due date:** 2016/09/27

## Specification

**Note: As of this assignment, we will be switching to use Python 3.**

Complete the following exercises, saving your solutions in the indicated files. For Python files that include test functions, GitHub will automatically run your tests with ```nosetests``` on every commit, indicating any failures via the Travis framework in the build status image above.

1. With your group, work through the [IPython and Jupyter slides](http://slides.com/profdressel/jupyter-overview) carefully, to make sure everything is now familiar. Be sure to use ```ipython3``` in a terminal to test how things work. Discuss amongst yourselves anything that is new or unclear.
1. Have one group member create a new Jupyter notebook ```cw04-primes.ipynb``` and open it within SageCloud. Go through the interface tutorial in the Help menu, as well as the key shortcuts. Note that the keys follow vim conventions. Use the template notebook in the info repository as a guide for how to format your notebook properly as a group. You will use this notebook to present your results for the classwork in a neat, clear, and professional way. Be sure to switch the default kernel to Python 3 instead of the default Python 2 used by Sage.
1. Create a new python module ```primes.py```. Be sure to use ```#!/usr/bin/env python3``` at the top to force use of Python 3. Inside this module create a function ```eratosthenes(n)```. This function will take a positive integer ```n``` and return all prime numbers smaller than ```n```. You should use the Sieve of Eratosthenes algorithm for computing these primes, which works as follows: First generate all positive integers less than ```n```, starting from the number 2. Then remove all multiples of 2. Then remove all multiples of the next largest remaining (prime) number. Then repeat the last step until you reach the largest remaining number. Finally, return the set of remaining (prime) numbers. Think carefully about which (basic) python data structure you want to use to implement this algorithm before you start coding.
1. Create a test function ```test_primes()``` that checks the output of ```eratosthenes(n)``` to ensure that it is correct.
1. Use a ```__main__``` section to make your python module executable as a script from the command line.
1. In your notebook, import the ```primes``` module at the top, and add a new section called "The Sieve of Eratosthenes". In this section, describe what the goal of the algorithm is, and how it works, in your own words. Describe your design decisions. Which data structure(s) did you use and why? Use $\LaTeX$ code as needed to format math in a pretty way in the notebook. Finally, create a code cell in the section that demonstrates the correct execution of your code.
1. In your primes module, create a new function ```gen_eratosthenes()``` that creates a generator for all the prime numbers. Rather than generating a fixed number as in the previous implementation, such a generator must produce one prime per iteration. Modify the algorithm to make this possible.
1. In your notebook, add a new section called "Generating Prime Numbers" that describes and demonstrates your new generator. Explain your design decisions, and what is different compared to the previous implementation.
1. In your notebook, add a new section called "Benchmarking Implementations". In this section, use the ```%time``` and ```%timeit``` magic commands to compare the efficiency of your implementations. Which is faster? By how much? Speculate about what is being slow about the slower implementation.
1. After your notebook is complete, spell-checked, and formatted properly, add and commit it to GitHub. Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having one person from your group be the official notebook editor, and having others in your group write code for the python modules in parallel.


## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have.

**This assignment was good to give us practice using markdown files and Jupyter. We did use ipython3 in the terminal to test out things as well, and there were some good interactive tutorials to get us used to it. We liked using implementing an algorithm as it gave us practicing with algorithms. The %time and %timeit was new, so we had to look it up on our own to figure how to use it. Perhaps a small tutorial or slide about it could help those of us who are unfamiliar with coding and not used to searching up answers online on our own. Other than that, I thought this assignment was great.**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.
* I also included this source in the module docstring that I used it for and explained how I used it:   http://codereview.stackexchange.com/questions/74550/prime-number-sequence-generator

Signed,

**Simrath Ratra, Afnan Alqahtani, Andrew nguyen**
