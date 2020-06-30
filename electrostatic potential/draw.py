import matplotlib.pyplot as plt
import numpy as np


a = open(r'./vplanar.txt', 'r').readlines()

a = [x.strip().split() for x in a]
i = 0

a1 = int(a[0][0])
a2 = int(a[0][1])
a3 = float(a[0][2])

x = []
y = []

for i in range(1, 1 + a1):
    x.append(a3 / a1 * int(a[i][0]))
    y.append(float(a[i][1]))

x = np.array(x)
y = np.array(y)

xmin, xmax = plt.xlim()
plt.axis([0, 29, -40, 10])

# plt.figure(figsize=())
plt.plot(x, y, 'k', linewidth=1.0)
# plt.savefig('./cb7.png', transparent=True, dpi=300)
plt.show()

