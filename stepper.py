import numpy as np

def shift(n=1):
    def stepper(swath):
        cs = swath
        while True:
            yield cs
            cs = np.roll(cs, 3*n)
    return stepper

def dimmer(n=1, steps=10):
    def stepper(swath):
        cs = np.copy(swath)
        ctr = 0
        while True:
            yield cs
            cs -= 1/steps; ctr += 1
            np.maximum(cs, 0, out=cs)
            if ctr >= steps:
                cs = np.copy(swath); ctr = 0
    return stepper
