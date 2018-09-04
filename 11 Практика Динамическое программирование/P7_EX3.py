def calculate_min_cost(n, price):
	C = [0]*(n + 1)
	C[1] = price[1]
	for i in range (2, n+1):
		C[i] = min(C[i-1], C[i-2]) + price[i]
	return C[n]



price = [i for i in range(10)]
n = 9
print(calculate_min_cost(n, price))
