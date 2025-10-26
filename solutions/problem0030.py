#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 30."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Digit Fifth Powers",
    "difficulty": 5,
    "description": r"""
        <p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
        $$\begin{align}
        1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
        8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
        9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
        \end{align}$$
        </p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
        <p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
        <p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>
    """,
    "answer": 443839,
}

def main():
    """Main function."""
    answer = sum(i for i in range(2, 6 * 9 ** 5 + 1) if i == sum(int(d) ** 5 for d in str(i)))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
