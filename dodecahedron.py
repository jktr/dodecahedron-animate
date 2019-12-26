import math
import numpy as np
from scipy.spatial import KDTree
import collections as coll


def euler_rodrigues_rotmat(axis, theta):
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(theta / 2.0)
    b, c, d = -axis * math.sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


def dodecahedron():
    phi = (1 + np.sqrt(5)) / 2
    a = [(x, y, z) for x in [-1,1] for y in [-1,1] for z in [-1,1]] \
        + [(x, y, z) for x in [0] for y in [-phi, phi] for z in [-1/phi,1/phi]] \
        + [(x, y, z) for x in [-1/phi,1/phi] for y in [0] for z in [-phi,phi]] \
        + [(x, y, z) for x in [-phi,phi] for y in [-1/phi,1/phi] for z in [0]]
    xs = np.array([x/phi for (x, _, _) in a])
    ys = np.array([y/phi for (_, y, _) in a])
    zs = np.array([z/phi for (_, _, z) in a])
    return np.array(list(zip(xs, ys, zs)))


def normalized(vs):
    rm = euler_rodrigues_rotmat([0, 1, 0], -(np.pi/3))
    return np.array([np.dot(rm, point) for point in vs])

def adjacency(vs):
    edges = coll.defaultdict(set)
    kdtree = KDTree(vs)
    for v in vs:
        ds, ns = kdtree.query(v, k=4)
        ds = ds[1:]
        ns = ns[1:]
        for d, n in zip(ds, ns):
            edges[tuple(v)].add(tuple(vs[n]))
    return edges


def ledify_edge(src, dst, n=50):
    xs = np.linspace(src[0], dst[0], n)
    ys = np.linspace(src[1], dst[1], n)
    zs = np.linspace(src[2], dst[2], n)
    return np.array(list(zip(xs, ys, zs)))
