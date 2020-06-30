def Solve(k, c, s):
  if c*s < k:
    return []  # returns an empty list for impossible cases
  tiles = []
  # the list for the last tile choice is filled with copies of k
  # i is the first value of the list of the current tile choice
  for i in xrange(1, k + 1, c):
    p = 1
    # j is the step in the current list [i, i+1, ..., i+C-1]
    for j in xrange(c):
      # the min fills the last tile choice's list with copies of k
      p = (p - 1) * k + min(i + j, k)
    tiles.append(p)
  return tiles

for i in range(1, 1 + input()):
  ca = raw_input().strip().split()
  ca = map(int, ca)

  #print ca
  print "Case #{}:".format(i),
  cz = Solve(ca[0], ca[1], ca[2])
  if cz == []:
    print "IMPOSSIBLE"
  else:
    print ' '.join(map(str, cz))
