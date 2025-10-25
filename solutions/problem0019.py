#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 19."""

# -----------------------------------------------------------------------------

from datetime import datetime


problem = {
    "title": "Counting Sundays",
    "difficulty": 5,
    "description": r"""
        <p>You are given the following information, but you may prefer to do some research for yourself.</p>
        <ul><li>1 Jan 1900 was a Monday.</li>
        <li>Thirty days has September,<br>
        April, June and November.<br>
        All the rest have thirty-one,<br>
        Saving February alone,<br>
        Which has twenty-eight, rain or shine.<br>
        And on leap years, twenty-nine.</li>
        <li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li>
        </ul><p>How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?</p>
    """,
    "answer": 171,
}

def main():
    """Main function."""
    answer = sum(datetime(y, m, 1).weekday() == 6 for y in range(1901, 2001) for m in range(1, 13))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
