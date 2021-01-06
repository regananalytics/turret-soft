# ERROR Mode
#   This is a catch-all error mode the turret enters if an error is raised
#   The error is logged and the turret then enters SHUTDOWN

import logging
from .mode import MODE

class ERROR(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='ERROR')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: Oh dear!")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
