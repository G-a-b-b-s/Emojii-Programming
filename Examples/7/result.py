def calculate_factorial(n):
	if n==0 :
		print("Factorial of 0 is 1")
		return

	result = 1
	for i in range(1, n+1):
		result = result*i
		print("Factorial is ", result)
calculate_factorial(5)
