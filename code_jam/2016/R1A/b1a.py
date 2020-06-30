for cas in xrange(1,1+input()):
    s = raw_input()
    def ans(j):
        if j == 0:
            return s[:j]
        else:
            x = max(s[:j])
            k = s.index(x)
            #for k in xrange(j):
            #    if s[k] == x:
            #        break
            l = []
            w = [ans(k)]
            for k in xrange(k,j):
                if s[k] == x:
                    l.append(x)
                else:
                    w.append(s[k])
            return ''.join(l + w)
    print "Case #%s: %s" % (cas, ans(len(s)))
