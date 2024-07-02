#!/usr/bin/python3
"""
Module for determining the winner where a prime nmber
along with its multiples are removed from the board
"""


def sieve_of_eratosthenes(max_n):
    """ Generates a list of primes up to max_n using the
    Sieve of Eratosthenes """
    is_prime = [True] * (max_n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= max_n:
        if is_prime[p]:
            for multiple in range(p * p, max_n + 1, p):
                is_prime[multiple] = False
        p += 1
    primes = [num for num, prime in enumerate(is_prime) if prime]
    return primes, is_prime


def isWinner(x, nums):
    """
    Determine the winner
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes, is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        primes_count = [0] * (n + 1)
        for i in range(1, n + 1):
            primes_count[i] = primes_count[i - 1] + (1 if is_prime[i] else 0)

        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
