#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
import numpy as np
import time
from fibonacci import fib_numba


def main():

	fib_n = np.linspace(30, 45, 16)
	t_c = []
	t_numb = []
	f = Person(0)
	for n in fib_n:
		f.set(int(n))
		s = time.perf_counter()
		f.fib()
		e = time.perf_counter()
		t_c.append(e - s)
  
		s = time.perf_counter()
		fib_numba(n)
		e = time.perf_counter()
		t_numb.append(e - s)


	plt.plot(fib_n,t_c, label = 'c++')
	plt.plot(fib_n,t_numb, label = 'numba')
	plt.legend()
	plt.title('comparisoin c++ and numba')
	plt.savefig('hoho_c++_numba.png')
	print('wow bild')

	print(fib_numba(47))
	f.set(int(47))
	print(f.fib())
	print()
 
if __name__ == '__main__':
	main()

#2971215073
#2971215073
#haha i made it long instead of int 