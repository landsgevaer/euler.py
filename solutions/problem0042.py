#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 42."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Coded Triangle Numbers",
    "difficulty": 5,
    "description": r"""
        <p>The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
        $$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
        <p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.</p>
        <p>Using <a href="resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p>
    """,
    "answer": 162,
}

def main():
    """Main function."""
    filename = __file__.replace("problem0042.py", "../files/0042_words.txt")
    with open(filename, "r", encoding="utf-8") as filehandle:
        words = filehandle.read()[1:-1].upper().split('","')
    wordsums = [sum(ord(letter) - 64 for letter in word) for word in words]
    max_wordsum = max(wordsums)
    triangles = set()
    triangle = n = 0
    while triangle < max_wordsum:
        n += 1
        triangle = n * (n + 1) // 2
        triangles.add(triangle)
    answer = sum(wordsum in triangles for wordsum in wordsums)
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
