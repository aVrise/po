import numpy as np

def f(fa, fb = 0):
    if len(fa) == 1:
        return fb if fa[0] == 1 else fb + 1
    else:
        return f(fa[1:], fb) if fa[0] == 1 else f(fa[::-1] * (-1), fb + 1)

for i in range(1, 1 + input()):
    ca = np.array([1 - 2 * (x == "-") for x in list(raw_input())])
    print ca
    print "Case #{}: {}".format(i,f(ca[::-1]))
