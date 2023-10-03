import matplotlib.pyplot as plt
import math
import random

n_lst = [1000, 10000, 100000]
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
i = 0

for n in n_lst:

    x_list = [random.uniform(-1,1) for _ in range(n)]
    y_list = [random.uniform(-1,1) for _ in range(n)]

    switch = 1
    x_s = []
    y_s = []
    x_c = []
    y_c = []
    n_c = 0

    for (x, y) in zip(x_list, y_list):
        r = math.sqrt(x**2+y**2)
        if r >= switch:
            x_s.append(x)
            y_s.append(y)
        else:
            x_c.append(x)
            y_c.append(y)
            n_c +=1

    axes[i].plot(x_c,y_c,'.',color = 'b')
    axes[i].plot(x_s,y_s,'.', color = 'r')
    i += 1
    print(f'number of points inside the circle for {n} points: {n_c}')
    _pi = 4*n_c/n
    print(f'approximation of pi for {n} points: {_pi}')
    
print(f'actuall PI {math.pi}')
plt.tight_layout()

plt.savefig('1.1.png')

plt.show()
