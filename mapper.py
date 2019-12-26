import numpy as np

def static():
    return (lambda swath, vs, ray: swath[:len(vs.T)])

# def combine(*mappers):
#     def mapper(swath, *args):
#         for m in mappers:
#             swath = m(swath, *args)
#         return swath
#     return mapper
            

def tracer(step=1):
    def mapper(swath, vs, _):
        return swath[:(len(vs.T))]
    return mapper

def random():
    def mapper(swath, vs, _):
        return np.array([swath[i] for i in
                         np.random.randint(len(swath), size=len(vs.T))])
    return mapper

def mirror(step=1):
    def mapper(swath, vs, _):
        c = swath[:(len(vs.T)//2)]
        return np.concatenate([c, c[::-1]])
    return mapper

def downpour(step=1, minz=-1, maxz=1):
    def mapper(swath, vs, _):
        l = len(swath)
        i = maxz-minz
        return np.array([swath[l-int((z+abs(minz))*l/i)] for z in vs[2]])
    return mapper

def sonar(step=1):
    def mapper(swath, vs, _):
        l = (len(swath)-1)/(np.pi*2)
        angle = np.arctan2(vs[1], vs[0])
        angle = angle + np.pi
        idx = np.asarray(angle * l, dtype=int)
        colors = np.array([swath[i] for i in idx])
        return colors
    return mapper
