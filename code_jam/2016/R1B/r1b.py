def f(fa):
    if ca[:fa] < cb[:fa]:
        return 0
    elif ca[:fa] > cb[:fa]:
        return 1
    else:
        return -1

def g(ga, gb):
    #print ga, gb
    if ga == gb and ga != len(ca):
        cagb = f(ga)
        if cagb == -1:
            ca[ga] = cb[gb] = '0'
        elif cagb == 0:
            ca[ga] = '9'
            cb[gb] = '0'
        else:
            ca[ga] = '0'
            cb[gb] = '9'
    elif ga < gb:
        cagb = f(ga)
        if cagb == -1:
            ca[ga] = cb[ga]
        elif cagb == 0:
            ca[ga] = '9'
        else:
            ca[ga] = '0'
    elif ga > gb:
        cagb = f(gb)
        if cagb == -1:
            cb[gb] = ca[gb]
        elif cagb == 0:
            cb[gb] = '0'
        else:
            cb[gb] = '9'


for i in range(1, 1 + input()):
    ca, cb = map(list, raw_input().strip().split())
    #print ca, cb
    cagb = -1
    # while '?' in ca:
    #     while '?' in cb:
    #         print i
    #         cai = ca.index('?') if '?' in ca else len(ca) + 1
    #         cbi = cb.index('?') if '?' in cb else len(cb) + 1
    #         g(cai, cbi)
    while True:
        #print i
        cai = ca.index('?') if '?' in ca else len(ca)
        cbi = cb.index('?') if '?' in cb else len(cb)
        g(cai, cbi)
        if cai == len(ca) and cbi == len(ca):
            break

    print "Case #{}: {} {}".format(i,''.join(ca), ''.join(cb))
