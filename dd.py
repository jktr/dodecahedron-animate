#!/usr/bin/env python3

import numpy as np
import collections as coll

import dodecahedron as ddh

from time import time

import segmentizer
import mapper
import swath
import stepper

import backend_mpl as virt

N = 10

vs = ddh.dodecahedron()
vs = ddh.normalized(vs)
edgemap = ddh.adjacency(vs)

ledmap = coll.defaultdict(list)
for k, vs in edgemap.items():
    for v in vs:
        ledmap[(k,v)].append(ddh.ledify_edge(k, v, N+2)[1:-1])

def animation(geometry, swath, stepper, mapper):
    segs, rays = geometry
    for step in stepper(swath):
        t = time()
        maps = [mapper(step, seg, ray) for seg, ray in zip(segs, rays)]
        print('frame', (time()-t)*1000)
        yield segs, rays, maps

def projector(segmentizer, swath, stepper, mapper):
    def ani(ledmap):
        segs, rays = segmentizer(ledmap)
        a = animation((segs, rays), swath, stepper, mapper)
        return a
    return ani


p = projector(
    segmentizer.fullseg_between_corners,

    #swath.wave(N, r=False, g=False, b=True),
    #swath.pulse(int(N), r=True, g=False, b=False),
    swath.rainbow(N),
    #swath.scanline(N),
    
    stepper.shift(),
    #stepper.dimmer(),

    #mapper.static(),
    mapper.sonar(),
    #mapper.downpour(),
    #mapper.mirror(),
    #mapper.random(),
    #mapper.tracer(),
)

virt.run(p(ledmap), N)
