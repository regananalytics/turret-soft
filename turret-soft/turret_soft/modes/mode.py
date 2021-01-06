import logging

# Mode class, which various modes will inherit from
class MODE:
    def __init__(self, *args, name='', **kwargs):
        self.name = name
        self.result = None

    def intro(self, *args, **kwargs):
        logging.info(f'Starting {self.name} mode.')
        return True

    def body(self, *args, **kwargs):
        logging.info(f'Running {self.name} mode.')
        return True

    def outro(self, *args, **kwargs):
        logging.info(f'Stopping {self.name} mode with result {self.result}.')
        return True

    def main(self, *args, **kwargs):
        # Main function logic
        if (result := self.intro(*args, **kwargs)):
            # If intro succeeds, run the body
            result = self.body(*args, **kwargs)
        # Save result
        self.result = result
        # Run outro always
        self.outro(*args, **kwargs)


