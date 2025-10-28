#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 43."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Sub-string Divisibility",
    "difficulty": 5,
    "description": r"""
        <p>The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.</p>
        <p>Let $d_1$ be the $1$<sup>st</sup> digit, $d_2$ be the $2$<sup>nd</sup> digit, and so on. In this way, we note the following:</p>
        <ul><li>$d_2d_3d_4=406$ is divisible by $2$</li>
        <li>$d_3d_4d_5=063$ is divisible by $3$</li>
        <li>$d_4d_5d_6=635$ is divisible by $5$</li>
        <li>$d_5d_6d_7=357$ is divisible by $7$</li>
        <li>$d_6d_7d_8=572$ is divisible by $11$</li>
        <li>$d_7d_8d_9=728$ is divisible by $13$</li>
        <li>$d_8d_9d_{10}=289$ is divisible by $17$</li>
        </ul><p>Find the sum of all $0$ to $9$ pandigital numbers with this property.</p>
    """,
    "answer": 16695334890,
}

def main():
    """Main function."""

    def recurse(number, depth=0):
        if depth == 7:
            return number
        total = 0
        for n in range(10):
            m = number * 10 + n
            if not (m % 1000) % mod[depth] and str(n) not in str(number):
                total += recurse(m, depth + 1)
        return total

    mod = [2, 3, 5, 7, 11, 13, 17]
    answer = 0
    for base in range(1000):
        if len(set(str(base))) == 3:
            answer += recurse(base)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
