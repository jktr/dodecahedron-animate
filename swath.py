import numpy as np

def rainbow(N):
    c = np.linspace(0,1,num=N)
    z = np.zeros(N)
    cs = np.concatenate([
        list(zip(c, c[::-1], z)),
        list(zip(c[::-1], z, c)),
        list(zip(z, c, c[::-1])),
    ], 0)
    return cs

def pulse(N, r=True, g=True, b=True):
    c = np.linspace(0,1,num=N)
    z = np.zeros(N)
    cs = np.concatenate([
        list(zip(c if r else z,
                 c if g else z,
                 c if b else z)),
        list(zip(z, z, z)),
    ], 0)
    return cs

def wave(N, r=True, g=True, b=True):
    c = np.linspace(0,1,num=N)
    z = np.zeros(N)
    cs = np.concatenate([
        list(zip(c if r else z,
                 c if g else z,
                 c if b else z)),
        list(zip(c[::-1] if r else z,
                 c[::-1] if g else z,
                 c[::-1] if b else z)),
    ], 0)
    return cs

def scanline(N, r=True, g=True, b=True):
    c = np.zeros(N)
    c[0] = 255
    z = np.zeros(N)
    cs = np.concatenate([
        list(zip(c if r else z,
                 c if g else z,
                 c if b else z)),
    ], 0)
    return cs
