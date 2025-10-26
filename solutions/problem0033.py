#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 33."""

# -----------------------------------------------------------------------------

from math import gcd


problem = {
    "title": "Digit Cancelling Fractions",
    "difficulty": 5,
    "description": r"""
        <p>The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9$s.</p>
        <p>We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.</p>
        <p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p>
        <p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p>
    """,
    "answer": 100,
}

def main():
    """Main function."""
    num = den = 1
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if a % 10 == 0 and b % 10 == 0:
                continue
            for digita in range(2):
                for digitb in range(2):
                    if str(a)[digita] == str(b)[digitb] and int(str(a)[1 - digita]) * b == int(str(b)[1 - digitb]) * a:
                        num *= a
                        den *= b
    answer = den // gcd(num, den)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
