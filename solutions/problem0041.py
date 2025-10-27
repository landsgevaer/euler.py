#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 41."""

# -----------------------------------------------------------------------------

from itertools import permutations
from problem0003 import is_prime


problem = {
    "title": "Pandigital Prime",
    "difficulty": 5,
    "description": r"""
        <p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
        <p>What is the largest $n$-digit pandigital prime that exists?</p>
    """,
    "answer": 7652413,
}

def main():
    """Main function."""
    answer = 0
    for digits in range(1, 10):
        if sum(range(1, digits + 1)) % 3:   # Digit-sum divisible by 3 cannot be prime
            for perm in permutations([str(i) for i in range(1, digits + 1)]):
                number = int(''.join(perm))
                if number > answer and is_prime(number):
                    answer = number
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
