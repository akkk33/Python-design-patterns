#!/usr/bin/python
"""
Decorator pattern
"""
__author__ = "Amr Khamis"
__copyright__ = "Copyright 2018"
__credits__ = [""]
__license__ = "GPL 3.0"
__version__ = "1.0"
__maintainer__ = "Amr Khamis"
__email__ = "akkk33@pm.me"
__status__ = "Production"


def wrapper(input_function):
    def post():
        input_function()
        print("Thanks for using our wrapper")

    return post()


@wrapper
def sum2():
    print(1 + 1)
