from typing import List


class LogicComponent(object):
    """
    A gate or other chip. Is instantiated with a `name` for debugging.
    Most components are built up from other components; some logic gates
    are implemented as base components, meaning their logic is written
    directly in Python rather than being composed of other components.
    """

    def __init__(self, name: str):
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
    InputPin) and for debugging. The Pin's `val` can be 1 or 0.
    """

    _val = 0

    def __init__(self, component: LogicComponent):
        self.component: LogicComponent = component

    def __str__(self):
        return f"{type(self).__name__}, val: {self._val}"

    def __repr__(self):
        return self.__str__()


class InputPin(Pin):
    """
    An InputPin provides a value to a LogicComponent and forces that
    component to evaluate (i.e. update its output based on its input).
    """

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val: int):
        # NOTE condition required to prevent loops in feedback circuits
        # this means that circuits cannot self-update from their initial
        # state - correct output levels must be set in init method
        if self._val != val:
            self._val = val

    def setExternalPin(self, val: int):
        """
        This is a convenience method for forcing evaluation to begin on
        an InputPin that is not connected on the left to any OutputPin.
        """
        self.val = val
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
    def val(self, val: int):
        if self._val != val:
            self._val = val
            for connection in self.connections:
                connection.val = val
            # TODO explain clearly why the second for loop is necessary
            for connection in self.connections:
                connection.component.evaluate()
