# IDLE Mode
#   IDLE mode is a motion detection state
#   The Turret will perform low framerate change detection mode
#   Success is achieved if threshold motion is detected, and the turret will enter TRACK mode
#   Failure continues IDLE mode

import logging
from .mode import MODE

class IDLE(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='IDLE')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: Are you there?")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
