import numpy as np


def get_random():
    a = round(np.random.random(), 4)
    return a


def fun(b):
    return 100 * b


def guess():
    c1 = get_random()
    c2 = fun(c1)
    return c1, c2


print(guess())
