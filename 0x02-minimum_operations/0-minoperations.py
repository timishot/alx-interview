#!/usr/bin/python3
"""
Minimun Operations Challenge
"""


def primeFactors(n):
    """
    Returns the prime factors of n
    """
    factors = []
    # Divide n by 2 until it is odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Try odd divisors from 3 to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 2
    # If n is still greater than 2, it is a prime factor
    if n > 2:
        factors.append(n)
    return factors


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    # If n is less than or equal to 1, return 0
    if n <= 1:
        return 0
    # Find the prime factors of n is now
    factors = primeFactors(n)
    return sum(factors)