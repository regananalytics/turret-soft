# TRACK Mode
#   TRACK mode is started after a successful detection in SEARCH mode
#   The Turret will attempt to track a detected object and calculate the object's path
#   Success is achieved if a path is calculated and the target is still in view
#   Failure sends the turret back into SEARCH mode

import logging
from .mode import MODE

class TRACK(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='TRACK')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: I see you!")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
