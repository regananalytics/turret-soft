import logging

from enum import Enum
from . import modes


class STATE(Enum):
    STARTUP = modes.STARTUP
    SEARCH = modes.SEARCH
    TRACK = modes.TRACK
    ENGAGE = modes.ENGAGE
    IDLE = modes.IDLE
    ERROR = modes.ERROR
    SHUTDOWN = modes.SHUTDOWN



class Turret:
    STATES = STATE

    def __init__(self, *args, **kwargs):
        logging.info('Initializing Turret')
        self._state = None
        self.state = self.STATES.STARTUP


    def run():
        mode = self.state.value
        return mode.run()


    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: STATE):
        self._state = new_state