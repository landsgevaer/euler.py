#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 20."""

# -----------------------------------------------------------------------------

from math import factorial


problem = {
    "title": "Factorial Digit Sum",
    "difficulty": 5,
    "description": r"""
        <p>$n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.</p>
        <p>For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.</p>
        <p>Find the sum of the digits in the number $100!$.</p>
    """,
    "answer": 648,
}

def main():
    """Main function."""
    answer = sum(int(s) for s in str(factorial(100)))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
