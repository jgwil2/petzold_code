# Charles Petzold's _Code_ in Python

This will be a Python implementation of the computer described in chapters 11-17 of _Code: The Hidden Language of Computer Hardware and Software_.

## Requirements

Python 3. This project has no dependencies outside the Python standard library.

## Run

`python -m unittest discover tests`

## Signal Propagation Model

This implementation takes logic gates as its most primitive objects, which can be "wired together" to create increasingly complex logic components. In order to simulate the behavior of these circuits, a simple digital model, in which a signal is either 1 (high) or 0 (low) is used. Components are connected via input and output pins, such that every input pins can be connected to output pins and changes in signals are propagated through the system, which can be seen as a directed graph (possibly containing cycles) of logic gates, useful configurations of which can be named and reused.

For more complex logic components, particularly those that have more than one stable state, it is important that the propagation of signals in the system happen in a breadth-first manner (in this simple model, connections are unweighted).

## Gates

The most basic object in this implementation is the logic gate. Following Petzold, we start with three primitive logic components implemented in Python: And, Or, and Not (plus one more for convenience: Buffer, which simply allows us to wire an output to multiple inputs). All other components are composed of these wired together in various configurations.

## Adders

The first machines assembled from gates are binary adding machines. A HalfAdder provides sum and carry outputs given two binary digits of input. A FullAdder provides sum and carry outputs given three input digits (two digits plus a carry digit from a less significant operation). FullAdders can be wired together to add two binary numbers of arbitrary size, and since we are building an 8-bit computer, we use eight of them to build an EightBitAdder.

## Flip-flops and Latches

These components allow us to build circuits with memory.
