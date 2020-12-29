'''
This script will check that tensorflow is installed
and is active in the current conda environment.
'''

try:
    import tensorflow as tf
    ver = tf.__version__
    print(f'\nTensorflow {ver} is installed and active.')
    print('You should be good to go!\n')
except:
    print('\nHmm...Something went wrong.\n' + \
        'I cannot seem to find tensorflow.\n' + \
        'Are you sure the right python interpretor is selected?\n')

print('End of Script.\n')