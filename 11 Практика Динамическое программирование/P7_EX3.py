def calculate_min_cost(n, price):
	C = [0]*(n + 1)
	C[0] = price[0]
	C[1] = price[1] + price[0]
	for i in range (2, n+1):
		C[i] = min(C[i-1], C[i-2]) + price[i]
	return C[n]



price = [1,2,8,1,12,2,5]
n = 6
print(calculate_min_cost(n, price))
