"""
Solutions to module 4
Student: Josefine Hörnell
Mail: josefine.honell@gmail.com
Reviewed by:
Reviewed date:
"""

import math
import random 
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future


def in_c(point):
    enough = 0
    for coord in point:
        enough += coord**2
    return math.sqrt(enough) <= 1
    
def cal_Vd_exp(n,d):
    d_list = []
    coord_list = []
    n_c = 0
    for i in range(d):
        new_list = [random.uniform(-1,1) for _ in range(n)]
        d_list.append(new_list)
        
    for dim in zip(*d_list):
        coord_list.append(dim)
        
    n_c = sum(list(map(in_c, coord_list)))
    
    Vd_exp = 2**d*n_c/n
    return Vd_exp  

if __name__ == "__main__":
    
    n = 10000000
    d = 11
    num_runs = 1
    
    start = pc()
    cal_Vd_exp(n,d)
    end = pc()

    print(f"Process took with no parallell programming {round(end-start, 2)/num_runs} seconds")
    num_runs_pal = 10
    n_pal = 1000000
    
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(cal_Vd_exp, n_pal, d) for _ in range(num_runs_pal)]
        results = [future.result() for future in future.as_completed(futures)]
    end = pc()
    print(f"Process took with  parallell programming {round(end-start, 2)/num_runs} seconds")

    Vd_exp = cal_Vd_exp(n,d)
    Vd_theory = math.pi**(d/2)/(math.gamma(d/2+1))
    print(f'the calculated V_d is {Vd_exp}')
    print(f'The theoretical V_d is {Vd_theory}')
    print(':)')
#for (100000,2)
# the calculated V_d is 3.14124
#The theoretical V_d is 3.141592653589793

#for (100000, 11)
#the calculated V_d is 1.92512
#The theoretical V_d is 1.8841038793898994

#Process took with no parallell programming 133.11 seconds
#Process took with  parallell programming 39.36 seconds
#It was about 70% faster than the non parallell one. 
#It is because it does the randomization and going through the 
#list as the same time instead of after one another
#why it isnt 10 times faster i believe is because of an icrease in
#start up time for parallell programming 