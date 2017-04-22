"""
This file should be used to complete Parts 2 and 3 in the Hackbright Prep loops
exercise. Part 1 may be completed in the Python interpreter.
"""

#####################################################################
# PART 2: For Loops


def print_1_to_10():
    """Prints out numbers from 1 to 10, not including 10.

    >>> print_1_to_10()
    1
    2
    3
    4
    5
    6
    7
    8
    9
    """
    # ADD YOUR FOR LOOP HERE
    for item in range(1, 10):
        print item


def print_10_to_15():
    """Prints out numbers from 10 to 15, exclusive, but prints 'hello' if the number is 13.

    >>> print_10_to_15()
    10
    11
    12
    hello
    14
    """
    # ADD YOUR CODE HERE
    for item in range(10, 15):
        if item == 13:
            print "hello"

        else:
            print item

def print_list_v1(fruits):
    """Prints out each item in a list, without using the range function.

    >>> fruits = ['apple', 'berry', 'cherry']
    >>> print_list_v1(fruits)
    apple
    berry
    cherry
    """
    # ADD YOUR CODE HERE
    pass


def print_list_v2(fruits):
    """Prints out each item in a list, using the range function.

    >>> fruits = ['apple', 'berry', 'cherry']
    >>> print_list_v2(fruits)
    apple
    berry
    cherry
    """
    # ADD YOUR CODE HERE
    pass


def sum_nums(num):
    """Add up all numbers from 0 to num, not inclusive, and prints the sum.

    Solve this without using Python's built-in sum() function.

    >>> sum_nums(8)
    28
    """
    # ADD YOUR CODE HERE
    pass


#####################################################################
# PART 3: While Loops

from random import randint


def guess_num():
    """Uses a while loop to prompt user to guess a secret number between 1 and 10."""

    random_integer = randint(1, 10)
    print "Random integer: ", random_integer

    # ADD YOUR WHILE LOOP HERE
    # guess_num = int(raw_input('Enter a number: '))

    while True:
        guess_num = int(raw_input('Enter a number: '))
        if guess_num < random_integer:
            print "too low"
            # guess_num = int(raw_input('Enter a number '))
        elif guess_num > random_integer:
            print 'too high'
            # guess_num = int(raw_input('Enter a number '))
        else: 
            print "you're right"
            break  
        


#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"