from enum import Enum
from typing import List


class Level(Enum):
    """
    Enumeration type for the value of a signal.
    """

    LO = 0
    HI = 1


class LogicComponent(object):
    """
    A gate or other chip. Is instantiated with a `name` for debugging.
    Most components are built up from other components; some logic gates
    are implemented as base components, meaning their logic is written
    directly in Python rather than being composed of other components.
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()

    def evaluate(self):
        """
        Must be implemented for base components - complex chips are
        just compositions of base components so they will automatically
        update their output signals when input signals change.
        """
        pass


class Pin(object):
    """
    Base class for a inputs and outputs. A Pin tracks its LogicComponent
    so that it can invoke the `evaluate` method (in the case of an
    InputPin) and for debugging. The Pin's `val` can be `HI` or `LO`.
    """

    def __init__(self, component: LogicComponent):
        self.component: LogicComponent = component

    _val = Level.LO


class InputPin(Pin):
    """
    An InputPin provides a value to a LogicComponent and forces that
    component to evaluate (i.e. update its output based on its input).
    """

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val: Level):
        self._val = val
        self.component.evaluate()


class OutputPin(Pin):
    """
    An OutputPin is assigned a value by a LogicComponent. It can be
    wired to one or more InputPins, whose value it updates whenever its
    own value is updated. These pins are tracked in the `connections`
    list.
    """

    def __init__(self, component):
        super().__init__(component)
        self.connections: List[InputPin] = []

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val: Level):
        self._val = val
        for connection in self.connections:
            connection.val = val
