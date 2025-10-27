#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 22."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Names Scores",
    "difficulty": 5,
    "description": r"""
        <p>Using <a href="resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.</p>
        <p>For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.</p>
        <p>What is the total of all the name scores in the file?</p>
    """,
    "answer": 871198282,
}

def main():
    """Main function."""
    filename = __file__.replace("problem0022.py", "../files/0022_names.txt")
    with open(filename, "r", encoding="utf-8") as filehandle:
        names = filehandle.read().upper().split(",")
    names.sort()
    answer = 0
    for index, name in enumerate(names, start=1):
        answer += index * sum(ord(letter) - 64 for letter in name.strip('"'))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
