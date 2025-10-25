#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 5."""

# -----------------------------------------------------------------------------

from math import gcd


problem = {
    "title": "Smallest Multiple",
    "difficulty": 5,
    "description": r"""
        <p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
        <p>What is the smallest positive number that is <strong>evenly divisible</strong> by all of the numbers from $1$ to $20$?</p>
    """,
    "answer": 232792560,
}

def main():
    """Main function."""
    answer = 1
    for factor in range(1, 21):
        answer *= factor // gcd(answer, factor)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
