from time import sleep
from src.base import LogicComponent, OutputPin


class Clock(LogicComponent):

    halt = False

    def __init__(self, name: str, frequency: int = 100):
        super().__init__(name)
        self.output = OutputPin(self)
        # default to 100 hertz
        self.interval = 1 / frequency

    def tick(self):
        self.output.val = 1
        sleep(self.interval)
        self.output.val = 0

    def oscillate(self):
        while True:
            self.tick()
            if self.halt:
                break
