#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 10."""

# -----------------------------------------------------------------------------

from problem0003 import generate_primes


problem = {
    "title": "Summation of Primes",
    "difficulty": 5,
    "description": r"""
        <p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
        <p>Find the sum of all the primes below two million.</p>
    """,
    "answer": 142913828922,
}

def main():
    """Main function."""
    answer = 0
    for prime in generate_primes():
        if prime >= 2000000:
            break
        answer += prime
    return answer

if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
