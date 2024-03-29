import math
import importlib
# import numpy as np 
from typing import *
from math import floor, ceil, sqrt

def package_exists(package: str) -> bool: 
	pkg_spec = importlib.util.find_spec(package)
	return(pkg_spec is not None)

def ask_package_install(package: str):
	if not(package_exists(package)):
		raise RuntimeError(f"Module {package} not installed. To use this function, please install {package}.")

## For counting function calls; boolean allows to turn off for non-benchmarking situations (production) 
## Inspired by both (1) and (2)
## 1. https://stackoverflow.com/questions/21716940/is-there-a-way-to-track-the-number-of-times-a-function-is-called
## 2. https://stackoverflow.com/questions/10724854/how-to-do-a-conditional-decorator-in-python
def counted(use: bool = True):
	def decorator(f: Callable): 
		if use: 
			def wrapped(*args, **kwargs):
				wrapped.calls += 1
				return f(*args, **kwargs)
			wrapped.calls = 0
			return(wrapped)
		else:
			return(f)
	return(decorator)

def inverse_choose(x: int, k: int):
	assert k >= 1, "k must be >= 1" 
	if k == 1: return(x)
	if k == 2:
		rng = range(int(floor(sqrt(2*x))), int(ceil(sqrt(2*x)+2) + 1))
		final_n = next(n for n in rng if math.comb(n, 2) == x)
		# final_n = rng[np.nonzero(np.array([math.comb(n, 2) for n in rng]) == x)[0].item()]
	else:
		# From: https://math.stackexchange.com/questions/103377/how-to-reverse-the-n-choose-k-formula
		if x < 10**7:
			lb = (math.factorial(k)*x)**(1/k)
			potential_n = list(range(int(floor(lb)), int(ceil(lb+k)+1)))
			final_n = next(n for n in potential_n if math.comb(n, k) == x) # potential_n[idx]
		else:
			lb = floor((4**k)/(2*k + 1))
			C, n = math.factorial(k)*x, 1
			while n**k < C: 
				n = n*2
			m = next(m**k for m in range(1, n+1) if x >= C)
			potential_n = range(int(max([m, 2*k])), int(m+k+1))
			final_n = next(n for n in potential_n if math.comb(n, k) == x)
	return(final_n)