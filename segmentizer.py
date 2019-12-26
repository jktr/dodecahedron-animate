import numpy as np

def halfray_from_corners(ledmap):
    # ledmap: 3,3 -> 3 N 3
    segments = []
    src = []
    for k, vss in ledmap.items():
        for vs in vss:
            vs = np.split(vs, 2)[0]
            vs = vs.T
            src.append(k)
            segments.append(vs)
    return np.array(segments), np.array(src)

def fullseg_between_corners(ledmap):
    # ledmap: 3,3 -> 3 N 3
    ledmap = {(tuple(np.minimum(k[0], k[1])),
               tuple(np.maximum(k[0], k[1]))): v for k, v in ledmap.items()}
    segments = []
    src = []
    for k, vss in ledmap.items():
        for vs in vss:
            vs = vs.T
            src.append(k)
            segments.append(vs)
    return np.array(segments), np.array(src)
