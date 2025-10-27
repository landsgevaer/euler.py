#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 39."""

# -----------------------------------------------------------------------------

from problem0009 import list_divisors


problem = {
    "title": "Integer Right Triangles",
    "difficulty": 5,
    "description": r"""
        <p>If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.</p>
        <p>$\{20,48,52\}$, $\{24,45,51\}$, $\{30,40,50\}$</p>
        <p>For which value of $p \le 1000$, is the number of solutions maximised?</p>
    """,
    "answer": 840,
}

def main():
    """Main function."""
    # a² + b² = (L - a - b)²  <=>  (a - L) (b - L) = ½L²
    answer = max_count = 0
    for L in range(2, 1001, 2):
        count = sum(L // 2 < factor < L for factor in list_divisors(L * L // 2))
        if count > max_count:
            answer = L
            max_count = count
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
