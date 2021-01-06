import asyncio
import logging

from .turret import Turret
from .utils.audio import AUDIO
from .utils.logging import fun_log


@fun_log
def main():
    pass #run_loop(Turret())
    

@fun_log
def run_loop(turret):
    while True:
        # Execute turret run, and break if it returns False
        if not turret.run():
            break


if __name__ == '__main__':
    main()