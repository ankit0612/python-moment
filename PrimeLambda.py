
primes=range(2,50)
for x in range(2,8):
	primes = filter(lambda i: i == x or i % x, primes)
print primes
