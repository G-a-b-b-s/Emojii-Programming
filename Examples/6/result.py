def calculate_fibonacci(n):
	if n==0 :
		print("Input must be greater than 0")
		return

	if n==2 :
		print(n)
		return

	a = 0
	b = 1
	for i in range(2, n+1):
		temp = a + b
		a = b
		b = temp
		print("Current Fibonacci value:", temp)
		print("Fibonacci value is ", b)
		calculate_fibonacci(10)
