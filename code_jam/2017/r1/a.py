def g(ga, gb):
    if ga[gb] == '?':
        if len(ga) - gb > ga[gb:].count('?'):
            return g(ga, gb + 1)
        else:
            return ga[gb-1]
    else:
        return ga[gb]

def f(fa):
    global ca
    if fa.count('?') == ca[1]:
        return fa
    else:
        while '?' in fa:
            fb = fa.index('?')
            fa[fb] = g(fa, fb)
        return fa

for i in range(1, 1 + input()):
    print "Case #{}:".format(i)
    ca = map(int, raw_input().split())
    cb = []
    for ci in range(ca[0]):
        cb += [list(raw_input())]
        cb[ci] = f(cb[ci])

    for ci in range(1, ca[0]):
        if '?' in cb[ci]:
            for cj in range(ca[1]):
                cb[ci][cj] = cb[ci - 1][cj]
    
    for ci in range(ca[0] - 2, -1, -1):
        if '?' in cb[ci]:
            for cj in range(ca[1]):
                cb[ci][cj] = cb[ci + 1][cj]

    for ci in range(ca[0]):
        print ''.join(cb[ci])
        