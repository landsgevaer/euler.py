#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 15."""

# -----------------------------------------------------------------------------

from math import comb


problem = {
    "title": "Lattice Paths",
    "difficulty": 5,
    "description": r"""
        <p>Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.</p>
        <div class="center">
        <img src="resources/images/0015.png?1678992052" class="dark_img" alt=""></div>
        <p>How many such routes are there through a $20 \times 20$ grid?</p>
    """,
    "answer": 137846528820,
}

def main():
    """Main function."""
    answer = comb(40, 20)
    return answer

if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
