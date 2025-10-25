#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 4."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Largest Palindrome Product",
    "difficulty": 5,
    "description": r"""
        <p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
        <p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
    """,
    "answer": 906609,
}

def main():
    """Main function."""
    answer = 0
    for number1 in range(100, 1000):
        for number2 in range(number1, 1000):
            product = number1 * number2
            if product > answer:
                palindrome = str(product)
                if palindrome == palindrome[::-1]:
                    answer = product
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
