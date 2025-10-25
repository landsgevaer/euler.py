#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Euler Project Problem 17."""

# -----------------------------------------------------------------------------

problem = {
    "title": "Number Letter Counts",
    "difficulty": 5,
    "description": r"""
        <p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
        <p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? </p>
        <br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.</p>
    """,
    "answer": 21124,
}

spoken_numbers = {
    'unit':
        ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
         "nineteen"),
    'decade':
        ("", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"),
    'postfix':
        ("", " thousand", " million", " billion", " trillion", " quadrillion", " quintillion"),
}

def speak_number(n, *, scale=0):
    """Returns the English spoken form of a number (up to 10^21) as a string."""
    if n < 20:
        return spoken_numbers['unit'][n] + spoken_numbers['postfix'][scale]
    if n < 100:
        return spoken_numbers['decade'][n // 10] \
             + ('-' + spoken_numbers['unit'][n % 10] if n % 10 else '') \
             + spoken_numbers['postfix'][scale]
    if n < 1000:
        return spoken_numbers['unit'][n // 100] + ' hundred' \
             + (' and ' + speak_number(n % 100) if n % 100 else '') \
             + spoken_numbers['postfix'][scale]
    return speak_number(n // 1000, scale=scale + 1) \
         + (' ' + speak_number(n % 1000) + spoken_numbers['postfix'][scale] if n % 1000 else '')

def main():
    """Main function."""
    answer = sum(char.isalpha() for number in range(1, 1001) for char in speak_number(number))
    return answer


if __name__ == "__main__":
    print(__doc__)
    print('"' + problem["title"] + '"')
    print("Expected answer:", problem["answer"])
    print("Computed answer:", main())
