#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 16."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Power Digit Sum",
    "difficulty": 5,
    "description": r"""
        <p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
        <p>What is the sum of the digits of the number $2^{1000}$?</p>
    """,
    "answer": 1366,
}

def main():
    """Main function."""
    answer = sum(int(i) for i in str(2**1000))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
