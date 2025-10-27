#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 37."""

# -----------------------------------------------------------------------------

from problem0003 import is_prime, generate_primes


problem = {
    "title": "Truncatable Primes",
    "difficulty": 5,
    "description": r"""
        <p>The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.</p>
        <p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p>
        <p class="smaller">NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.</p>
    """,
    "answer": 748317,
}

def main():
    """Main function."""
    count = answer = 0
    for p in generate_primes():
        if p < 10:
            continue
        digits = str(p)
        valid = True
        for i in range(1, len(digits)):
            valid = valid and is_prime(int(digits[i:])) and is_prime(int(digits[:-i]))
        if valid:
            answer += p
            count += 1
            if count == 11:
                break
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
