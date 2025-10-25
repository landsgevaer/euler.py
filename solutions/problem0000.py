#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 0."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Problem Zero",
    "difficulty": 5,
    "description": r"""
        <p>A number is a perfect square, or a square number, if it is the square of a positive integer.<br>
        For example, $25$ is a square number because $5^2 = 5 \times 5 = 25$; it is also an odd square.</p>
        <p>The first 5 square numbers are: $1, 4, 9, 16, 25$, and the sum of the odd squares is $1 + 9 + 25 = 35$.</p>
        <p>Among the first <strong>100 thousand</strong> square numbers, what is the sum of all the odd squares?</p>
    """,
    "answer": 166666666650000,
}

def main():
    """Main function."""
    answer = sum(i ** 2 for i in range(1, 100000, 2))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
