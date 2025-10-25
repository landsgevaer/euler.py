#!/usr/bin/env python3
# *_* coding: utf-8 *_*

"""Main script, runs all Euler problems and reports results."""

__version__ = "0.1"
__author__ = "Dave R.M. Langers"
__email__ = "dave@langers.nl"
__copyright__ = "Copyright (c) 2025, Dave R.M. Langers"
__license__ = "MIT"

# -----------------------------------------------------------------------------

from glob import glob
from importlib import import_module
from inspect import getmodule, signature
from re import sub, DOTALL, MULTILINE
from sys import argv, path
from time import perf_counter


def get_functions(module):
    """Returns information about helper functions in a given module."""
    functions = []
    for attr in dir(module):
        member = getattr(module, attr)
        if callable(member) and getmodule(member) == module and member.__name__ != "main":
            functions.append({
                "Module": module.__name__,
                "Function": member.__name__ + str(signature(member)),
                "Description": member.__doc__,
            })
    return functions

def get_solution(module):
    """Returns information about the solution in a given module."""
    time = perf_counter()
    answer = module.main()
    time = (perf_counter() - time) * 1e3
    return {
        "ID": int(module.__name__.removeprefix("problem")),
        "Lvl": module.problem["difficulty"],
        "Title": module.problem["title"],
        "Answer": answer,
        "✔/✘": "✔" if answer == module.problem["answer"] else "✘",
        "Time [ms]": round(time, 1),
    }

def make_table(data, align):
    """Turns a list of dicts into a markdown table with given alignments."""

    def make_row(items):
        return "| " + " | ".join(items) + " |\n"

    width = {key: len(key) for key in align}
    for item in data:
        for key, value in item.items():
            width[key] = max(width[key], len(str(value)))
    table = make_row(f"{key:{align[key]}{width[key]}}" for key in align) \
          + make_row(":" + "-" * (width[key]-1) if align[key] == "<" else
                              "-" * (width[key]-1) + ":" if align[key] == ">" else
                              ":" + "-" * (width[key]-2) + ":" for key in align)
    for item in data:
        table += make_row(f"{val:{align[key]}{width[key]}}" for key, val in item.items())
    return table.rstrip()

def main(results):
    """Main function."""
    if not results:
        results = "results.md"
    functions, solutions = [], []
    path.append("solutions")
    for filename in sorted(glob("problem????.py", root_dir="solutions")):
        module = import_module(filename.removesuffix(".py"))
        functions.extend(get_functions(module))
        solutions.append(get_solution(module))
    with open("README.md", "r", encoding="utf-8") as filehandle:
        readme = filehandle.read()
    with open("README.md", "w", encoding="utf-8") as filehandle:
        table = make_table(functions, {
                "Module": "<",
                "Function": "<",
                "Description": "<"}
        )
        filehandle.write(sub(
            r"(\[]\(#start-helper-table\)\n\n).*(\n\n\[]\(#end-helper-table\))",
            r"\1" + table + r"\2",
            readme,
            flags=MULTILINE | DOTALL
        ))
    table = make_table(solutions, {
            "ID": ">",
            "Lvl": "^",
            "Title": "<",
            "Answer": ">",
            "✔/✘": "^",
            "Time [ms]": ">"
        })
    with open(results, "w", encoding="utf-8") as filehandle:
        filehandle.write(table)
    print(table)
    return 0


if __name__ == "__main__":
    main(argv[1] if len(argv) > 1 else "")
