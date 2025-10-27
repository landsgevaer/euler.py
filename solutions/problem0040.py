#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 40."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Champernowne's Constant",
    "difficulty": 5,
    "description": r"""
        <p>An irrational decimal fraction is created by concatenating the positive integers:
        $$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$</p>
        <p>It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.</p>
        <p>If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
        $$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$</p>
    """,
    "answer": 210,
}

def generate_champernowne():
    """Generator of champernowne constant decimals."""
    n = 0
    while True:
        n += 1
        for d in str(n):
            yield int(d)

def main():
    """Main function."""
    target = product = 1
    for index, digit in enumerate(generate_champernowne(), start=1):
        if index == target:
            product *= digit
            target *= 10
            if target > 1000000:
                break
    return product


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
