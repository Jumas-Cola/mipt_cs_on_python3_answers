import sys

def fac(n, depth=0):
	if n == 0:
		print('Depth: '+str(depth))
		return 1
	else:
		depth+=1
		return n * fac(n - 1, depth)

print(sys.getrecursionlimit())
print(fac(994))