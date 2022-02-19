"""
Created on Sep 30, 2016

@author: Arthur
"""

'''
    1. Write a test function
'''


def test_gcd():
    assert gcd(0, 2) == 2
    assert gcd(2, 0) == 2
    assert gcd(1, 2) == 1
    assert gcd(2, 1) == 1
    assert gcd(6, 2) == 2
    assert gcd(6, 3) == 3
    assert gcd(21, 2) == 1
    assert gcd(2, 21) == 1
    assert gcd(210, 15) == 15
    assert gcd(15, 210) == 15


'''
    Write a first version of the function
'''


def gcd(a, b):
    """
    Calculates the GCD of a and b
    a,b - input integers, a,b >= 0
    Returns the GCD of positive integers a and b
    """
    pass


'''
    2. Run the test function.
    
    NB!
    If it passes, you've done something wrong :-)
'''
test_gcd()

'''
    3. Write the gcd function according to its specification
'''
# def gcd(a, b):
#     '''
#     Calculates the GCD of a and b
#     a,b - input integers, a,b >= 0
#     Returns the GCD of positive integers a and b
#     '''
#     if a == 0:
#         return b
#     if b == 0:
#         return a
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a

'''
    4. Run the test(s) again
    
    NB!
    If they fail, you've done something wrong :-<
'''
# test_gcd()


'''
    5. Refactor / optimize the function 
'''
