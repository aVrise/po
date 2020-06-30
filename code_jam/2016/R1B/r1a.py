def f(fa):
    return ca.count(fa) if fa in ca else 0

for i in range(1, 1 + input()):
    ca = raw_input()

    zero = f('Z')
    two = f('W')
    four = f('U')
    six = f('X')
    eight = f('G')
    five = ca.count('F') - four
    seven = ca.count('S') - six
    three = ca.count('H') - eight
    one = ca.count('O') - zero - two - four
    nine = ca.count('E') - zero - one - 2 * three - five - 2 * seven - eight

    ans = zero * ['0'] + one * ['1'] + two * ['2'] + three * ['3'] + four * ['4'] + five * ['5'] + six * ['6'] + seven * ['7'] + eight * ['8'] + nine * ['9']

    print "Case #{}: {}".format(i,''.join(ans))
