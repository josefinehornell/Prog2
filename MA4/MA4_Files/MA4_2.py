#!/usr/bin/env python3.9

from person import Person
import matplotlib.pyplot as plt
import numpy as np
import time


def main():

	N = np.linspace(30, 45, 16)
	T = []
	f = Person(0)
	for x in N:
		f.set(int(x))
		start = time.perf_counter()
		f.fib()
		stop = time.perf_counter()
		T.append(stop - start)

	plt.plot(N,T)
	plt.title('c++')
	plt.savefig('c++.png')

if __name__ == '__main__':
	main()
