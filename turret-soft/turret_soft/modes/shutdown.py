# SHUTDOWN Mode
#   SHUTDOWN mode performs the necessary actions to shutdown the turret

import logging
from .mode import MODE

class SHUTDOWN(MODE):

    def __init__(self, **kwargs):
        super().__init__(self, name='SHUTDOWN')

    
    def entry(self, *args, **kwargs):
        super().entry(self, *args, **kwargs)
        print("TURRET: Shutting down.")
        self.result = True


    def exit(self, *args, **kwargs):
        super().exit(self, *args, **kwargs)
        return self.result
