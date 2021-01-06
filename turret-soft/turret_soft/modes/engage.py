# ENGAGE Mode
#   This is the first operation mode when the turret starts up.
#   We'll initialize anything we need to here like loading up our tensorflow model.
#   Then we will move to the "search" operation mode.

import logging
from .mode import MODE

class ENGAGE(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='ENGAGE')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: Fire!")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
