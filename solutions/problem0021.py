#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 21."""

# -----------------------------------------------------------------------------

from problem0009 import list_divisors


problem = {
    "title": "Amicable Numbers",
    "difficulty": 5,
    "description": r"""
        <p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
        If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
        <p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
        <p>Evaluate the sum of all the amicable numbers under $10000$.</p>
    """,
    "answer": 31626,
}

def main():
    """Main function."""
    answer = 0
    for a in range(2, 10000):
        b = sum(list_divisors(a)) - a
        if a != b and sum(list_divisors(b)) - b == a:
            answer += a
    return answer

if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
