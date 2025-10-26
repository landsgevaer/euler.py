#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 34."""

# -----------------------------------------------------------------------------

from itertools import combinations_with_replacement
from math import factorial


problem = {
    "title": "Digit Factorials",
    "difficulty": 5,
    "description": r"""
        <p>$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.</p>
        <p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p>
        <p class="smaller">Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.</p>
    """,
    "answer": 40730,
}

def main():
    """Main function."""
    answer = 0
    for length in range(2, 8):
        for digits1 in combinations_with_replacement(range(10), length):
            digits1 = list(digits1)
            number = sum(factorial(digit) for digit in digits1)
            digits2 = [int(d) for d in str(number)]
            digits2.sort()
            if digits1 == digits2:
                answer += number
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
