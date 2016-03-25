# Takes my num an integer and it returns true if its prime
# It returns false if its not prime
# do range from 1 and

def isPrime(x, list):
	y = range(1,int(x))
	num = x - 2
	# make a loop

	for num in y:
		zero = 0
		myRem = int(x) % int(num)
		
		if myRem !=0:
			zero = zero + 1	
		if zero == num:
			print(x)
			list.append(x)
listt =[]
thePrimes = open=("primes.txt", "w")
listOfR = range(2, 10000)

for s in listOfR:
	recentNum = isPrime(s, listt)

for y in listt:
	thePrimes.write(str(y) +"/n")
thePrimes.close()
