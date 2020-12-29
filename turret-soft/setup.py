from setuptools import setup, find_packages
from . import __about__

setup(
    name='turret-soft',
    version=__about__.__version__,
    pacakges=find_packages(),
    entry_points={
        'console_scripts': [
            'turret = turret_soft.__main__:main'
        ]
    },
    install_requires={
        'tensorflow',
    }
)