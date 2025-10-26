#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 28."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Number Spiral Diagonals",
    "difficulty": 5,
    "description": r"""
        <p>Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:</p>
        <p class="monospace center">
        21 22 23 24 25<br>
        20  7  8  9 10<br>
        19  6  1  2 11<br>
        18  5  4  3 12<br>
        17 16 15 14 13</p>
        <p>It can be verified that the sum of the numbers on the diagonals is $101$.</p>
        <p>What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?</p>
    """,
    "answer": 669171001,
}

def main():
    """Main function."""
    bottomright = sum(4 * i * i + 6 * i + 3 for i in range(500))
    bottomleft = sum(4 * i * i + 8 * i + 5 for i in range(500))
    topleft = sum(4 * i * i + 10 * i + 7 for i in range(500))
    topright = sum(4 * i * i + 12 * i + 9 for i in range(500))
    answer = 1 + bottomright + bottomleft + topleft + topright
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
