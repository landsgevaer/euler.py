#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 6."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Sum Square Difference",
    "difficulty": 5,
    "description": r"""
        <p>The sum of the squares of the first ten natural numbers is,</p>
        $$1^2 + 2^2 + ... + 10^2 = 385.$$
        <p>The square of the sum of the first ten natural numbers is,</p>
        $$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
        <p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
        <p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
    """,
    "answer": 25164150,
}

def main():
    """Main function."""
    answer = sum(range(1, 101)) ** 2 - sum(i ** 2 for i in range(1, 101))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
