#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 24."""

# -----------------------------------------------------------------------------

from itertools import permutations


problem = {
    "title": "Lexicographic Permutations",
    "difficulty": 5,
    "description": r"""
        <p>A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:</p>
        <p class="center">012   021   102   120   201   210</p>
        <p>What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?</p>
    """,
    "answer": 2783915460,
}

def main():
    """Main function."""
    for index, permutation in enumerate(permutations(range(10)), start=1):
        if index == 1000000:
            return int(''.join(str(i) for i in permutation))


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
