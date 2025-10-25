#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 1."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Multiples of 3 or 5",
    "difficulty": 5,
    "description": r"""
        <p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
        <p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
    """,
    "answer": 233168,
}

def main():
    """Main function."""
    answer = sum(i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
