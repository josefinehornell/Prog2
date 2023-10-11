from numba import njit
import time
import matplotlib.pyplot as plt

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
    
@njit    
def fib_numba(n):
    if n <= 1:
        return n
    else:
        return(fib_numba(n-1) + fib_numba(n-2))
    

py_t_lst = []
num_t_lst = []
fib_lst = [x for x in range(20, 31)]

for n in fib_lst:
    s = time.time()
    fib_numba(n)
    e = time.time()
    t_time = e - s 
    num_t_lst.append(t_time)  
    
    s = time.time()
    fib_py(n)
    e = time.time()
    t_time = e - s  
    py_t_lst.append(t_time)

#plt.plot(fib_lst, py_t_lst, label = 'python')
#plt.plot(fib_lst, num_t_lst, label = 'numba')
#plt.legend()
#plt.savefig('fib_py_numba.png')
#plt.show()