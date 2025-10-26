#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 32."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Pandigital Products",
    "difficulty": 5,
    "description": r"""
        <p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.</p>
        <p>The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.</p>
        <p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.</p>
        <div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>
    """,
    "answer": 45228,
}

def main():
    """Main function."""
    products = set()
    for a in range(1, 100):
        for b in range(a + 1, 10000):
            digits = str(a) + str(b) + str(a * b)
            if len(digits) == 9:
                digits = list(digits)
                digits.sort()
                if digits == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    products.add(a * b)
    answer = sum(products)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
