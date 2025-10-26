#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 31."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Coin Sums",
    "difficulty": 5,
    "description": r"""
        <p>In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:</p>
        <blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote>
        <p>It is possible to make £2 in the following way:</p>
        <blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote>
        <p>How many different ways can £2 be made using any number of coins?</p>
    """,
    "answer": 73682,
}

def count_partitions(n, *, allowed=None):
    """Count how many ways an integer n can be partitioned into numbers from a set."""
    if allowed is None:
        allowed = set(range(1, n))
        number = n
    elif allowed:
        allowed = allowed.copy()
        number = allowed.pop()
    else:
        return int(n == 0)
    return sum(count_partitions(n - i * number, allowed=allowed) for i in range(n // number + 1))

def main():
    """Main function."""
    answer = count_partitions(200, allowed={1, 2, 5, 10, 20, 50, 100, 200})
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
