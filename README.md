# euler.py
Project Euler in Python

![version](https://img.shields.io/badge/version-0.1-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)

[Project Euler](https://projecteuler.net/) is a series of challenging mathematical/computer programming problems that
will require more than just mathematical insights to solve. Although mathematics will help you arrive at elegant and
efficient methods, the use of a computer and programming skills will be required to solve most problems.

This repository contains a collection of hand-crafted solutions to these problems in the Python 3 programming language,
using only built-in functions and modules from the [Python Standard Library](https://docs.python.org/3/library/). There
are no further dependencies.

⚠️ This repository contains spoilers. Please refrain from using it if you wish to solve the problems yourself.

The various solutions all contain a `main()` function that computes the solution, plus potentially a set of helper
functions that performs general tasks. The latter are often imported and re-used in solutions to later problems. These
may also be useful to you; for an overview of these, see the table under [Execution / Usage](#execution--usage).


**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)


## Installation

Assuming you have Python 3.x installed, simply clone the repository from a terminal, and you are ready to go:

```sh
git clone https://github.com/landsgevaer/euler.py
```

⚠️ The codebase was tested using Python 3.12 but should work on various earlier versions as well.


## Execution / Usage

To run the main script, fire up a terminal window and run the following command:

```sh
python3 main.py
```

This will run all available solutions to solved problems, verify their correctness, measure their runtime, and show an
overview of the results in the terminal. The results will also be written to a file `results.md` (you may specify a
different filename by providing it as a command-line argument, like `python3 main.py my_output.md`).

⚠️ This script will also automatically update the overview of helper functions in this `README.md` file.

You may also run a single solution separately using a command like:

```sh
python3 solutions/problem0000.py
```

The problems are numbered according to the problem ID on the [Problem Archives](https://projecteuler.net/archives).
Problem 0 refers to the problem posed when [registering](https://projecteuler.net/register) (note that the numbers in
problem 0 are randomised for each visitor).

The following helper functions are provided in the various solutions:

[](#start-helper-table)

| Module      | Function             | Description                     |
| :---------- | :------------------- | :------------------------------ |
| problem0002 | generate_fibonacci() | Generator of Fibonacci numbers. |

[](#end-helper-table)


## Contributing

Because this is a personal project to challenge myself to solve all problems in the Euler Project, no pull requests will
be accepted. You are of course free to be inspired by this repository and improve on its solutions yourself. In case of
questions or comments on the solutions, feel free to contact me (see the [author details](#Author) below).


## Author

Dave R.M. Langers – [@landsgevaer](https://github.com/landsgevaer) – [dave@langers.nl](mailto:dave@langers.nl)


## License

"Project Euler in Python" is distributed under the MIT-license. See [`LICENSE`](LICENSE) for more details.
