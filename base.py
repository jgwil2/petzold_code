from enum import Enum
from typing import List


class Level(Enum):
    LO = 0
    HI = 1


class LogicComponent(object):
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
        emit update their output signals when input signals change
        """
        pass


class Pin(object):
    def __init__(self, component: LogicComponent):
        self.component: LogicComponent = component

    _val = Level.LO


class InputPin(Pin):
    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val: Level):
        self._val = val
        self.component.evaluate()


class OutputPin(Pin):
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
