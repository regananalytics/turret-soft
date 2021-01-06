import functools
import logging

# Set logging level to DEBUG for now and set up some formatting
logging.basicConfig(
    filename='turret.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(levelname)s : %(asctime)s :: %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p')


def fun_log(fun):
    mod_name = fun.__module__
    fun_name = fun.__name__
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        logging.info(f'Entering function {fun_name} in {mod_name}')
        return fun(*args, **kwargs)
    return wrapper