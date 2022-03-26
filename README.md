# Charles Petzold's _Code_ in Python

This will be a Python implementation of the computer described in chapters 11-17 of _Code: The Hidden Language of Computer Hardware and Software_.

## Requirements

Python 3. This project has no dependencies outside the Python standard library.

## Run

`python -m unittest discover tests`

## Gates

The most basic object in this implementation is the logic gate. Following Petzold, we start with three primitive logic components implemented in Python: And, Or, and Not (plus one more for convenience: Relay, which simply allows us to wire an output to multiple inputs). All other components are composed of these wired together in various configurations.
