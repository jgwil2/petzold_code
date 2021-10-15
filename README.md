# Charles Petzold's _Code_ in Python

This will be a Python implementation of the computer described in chapters 11-19 of _Code: The Hidden Language of Computer Hardware and Software_.

## Gates

The most basic object in this implementation is the logic gate. Following Petzold, we start with three primitive logic components implemented in Python: And, Or, and Not (plus one more for convenience: Split, which simply allows us to wire an output to multiple inputs). All other components are composed of these wired together in various configurations.

## Notes

We don't actually need Splitter class - could be simplified to just Relay (or is there a better name?), where output = input, because output pins already support multiple connections.
