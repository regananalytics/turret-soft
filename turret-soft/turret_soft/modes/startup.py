# STARTUP Mode
#   This is the first operation mode when the turret starts up.
#   We'll initialize anything we need to here like loading up our tensorflow model.
#   Success is achieved after initialization steps are complete, and turret enters SEARCH mode
#   Failure to initialize causes the turret to SHUTDOWN

import logging
from .mode import MODE

class STARTUP(MODE):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, name='STARTUP', **kwargs)


    def intro(self, *args, **kwargs):
        pass

    def body(self, *args, **kwargs):
        pass

    def outro(self, *args, **kwargs):
        pass