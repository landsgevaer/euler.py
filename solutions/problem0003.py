#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 3."""

# -----------------------------------------------------------------------------

from itertools import count


problem = {
    "title": "Largest Prime Factor",
    "difficulty": 5,
    "description": r"""
        <p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
        <p>What is the largest prime factor of the number $600851475143$?</p>
    """,
    "answer": 6857,
}

prime_cache = [2, 3, 5]

def generate_primes():
    """Generator of prime numbers."""
    for index in count():
        if index >= len(prime_cache):
            n = prime_cache[-1] + 2
            while not is_prime(n):
                n += 2
            prime_cache.append(n)
        yield prime_cache[index]

def is_prime(number):
    """Determine whether a number is prime."""
    lgN = len(prime_cache).bit_length()
    if prime_cache[lgN] ** 2 - 2 < number < prime_cache[-1] + 2:
        # Bisection; takes O(lg(N)) steps.
        lo, hi = lgN, len(prime_cache) - 1
        while lo < hi:
            md = (lo + hi) // 2
            if number < prime_cache[md]:
                hi = md - 1
            elif number > prime_cache[md]:
                lo = md + 1
            else:
                return True
        return number == prime_cache[lo]
    for prime in generate_primes():
        # Sieve; takes O(sqrt(n)) steps.
        if number % prime == 0:
            return False
        if prime * prime > number:
            return True

def factorize_primes(n):
    """Decompose a number into prime factors with their exponents."""
    decomposition = {}
    for prime in generate_primes():
        while not n % prime:
            n //= prime
            decomposition[prime] = decomposition.get(prime, 0) + 1
        if prime * prime > n:
            if n > 1:
                decomposition[n] = 1
            break
    return decomposition

def main():
    """Main function."""
    answer = max(factorize_primes(600851475143).keys())
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
