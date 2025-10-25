#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 9."""

# -----------------------------------------------------------------------------

from problem0003 import factorize_primes


problem = {
    "title": "Special Pythagorean Triplet",
    "difficulty": 5,
    "description": r"""
        <p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
        $$a^2 + b^2 = c^2.$$</p>
        <p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
        <p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.</p> 
    """,
    "answer": 31875000,
}

def list_divisors(n):
    """List all divisors of n."""
    result = [1]
    for prime, power in factorize_primes(n).items():
        length = len(result)
        for _ in range(length * power):
            result.append(result[-length] * prime)
    result.sort()
    return result

def main():
    """Main function."""
    # a² + b² = (L - a - b)²  <=>  (a - L) (b - L) = ½L²
    for factor1 in list_divisors(500000):
        factor2 = 500000 // factor1
        if factor1 < 1000 and factor2 < 1000:
            a, b, c = 1000 - factor1, 1000 - factor2, factor1 + factor2 - 1000
            answer = a * b * c
            return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
