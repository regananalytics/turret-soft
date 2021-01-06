# SEARCH Mode
#   SEARCH mode is the object detection mode
#   The Turret will attempt to detected objects in its view
#   Success is achieved if an object is detected, and the turret will enter TRACK mode
#   Failure occurs if nothing is discovered after a TIMEOUT period, and the turret enters IDLE mode

import logging
from .mode import MODE

class SEARCH(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='SEARCH')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: Are you there?")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
