nterms = int(input("Enter the number of terms: "))

def loop(n):
	if n > 0:
		loop(n-1)
		print(n)

loop(nterms)