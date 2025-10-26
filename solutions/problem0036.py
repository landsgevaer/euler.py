#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 36."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Double-base Palindromes",
    "difficulty": 5,
    "description": r"""
        <p>The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.</p>
        <p>Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.</p>
        <p class="smaller">(Please note that the palindromic number, in either base, may not include leading zeros.)</p>
    """,
    "answer": 872187,
}

def main():
    """Main function."""
    answer = 0
    for i in range(1, 1000000):
        base10 = str(i)
        base2 = bin(i)[2:]
        if base10 == base10[::-1] and base2 == base2[::-1]:
            answer += i
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
