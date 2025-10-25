#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 7."""

# -----------------------------------------------------------------------------

from problem0003 import generate_primes


problem = {
    "title": "10 001st Prime",
    "difficulty": 5,
    "description": r"""
        <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
        <p>What is the $10\,001$st prime number?</p>
    """,
    "answer": 104743,
}

def main():
    """Main function."""
    for index, answer in enumerate(generate_primes(), start=1):
        if index == 10001:
            return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
