#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 35."""

# -----------------------------------------------------------------------------

from problem0003 import is_prime, generate_primes


problem = {
    "title": "Circular Primes",
    "difficulty": 5,
    "description": r"""
        <p>The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.</p>
        <p>There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.</p>
        <p>How many circular primes are there below one million?</p>
    """,
    "answer": 55,
}

def main():
    """Main function."""
    answer = 0
    for p in generate_primes():
        if p >= 1000000:
            break
        digits = str(p)
        valid = True
        for _ in range(len(digits) - 1):
            digits = digits[-1] + digits[:-1]
            valid = valid and is_prime(int(digits))
        answer += valid
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())