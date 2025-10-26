#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 14."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Longest Collatz Sequence",
    "difficulty": 5,
    "description": r"""
        <p>The following iterative sequence is defined for the set of positive integers:</p>
        <ul style="list-style-type:none;">
        <li>$n \to n/2$ ($n$ is even)</li>
        <li>$n \to 3n + 1$ ($n$ is odd)</li></ul>
        <p>Using the rule above and starting with $13$, we generate the following sequence:
        $$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$</p>
        <p>It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.</p>
        <p>Which starting number, under one million, produces the longest chain?</p>
        <p class="note"><b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.</p>
    """,
    "answer": 837799,
}

def generate_collatz(n):
    """Generator of Collatz sequence."""
    yield n
    while n > 1:
        n = 3 * n + 1 if n % 2 else n // 2
        yield n

def main():
    """Main function."""
    lengths = [0] * 1000000
    lengths[1] = 1
    for number in range(2, 1000000):
        if not lengths[number]:
            collatz = []
            for n in generate_collatz(number):
                collatz.append(n)
                if n < 1000000 and lengths[n]:
                    break
            for i, n in enumerate(collatz, start=1):
                if n < 1000000:
                    lengths[n] = lengths[collatz[-1]] + len(collatz) - i
    answer = max(enumerate(lengths), key=lambda x: x[1])[0]
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
