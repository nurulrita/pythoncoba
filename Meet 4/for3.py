b = input ("masukan angka maks: ")
for b in range (1, b+1):
    if b % 3 == 0 and b % 5 == 0: # % adalah mod, sisa dari pembagian
         print "FizzBuzz"
    elif b % 3 == 0:
         print "Buzz"
    elif b % 5 == 0:
         print "Fizz"
    else: 
	 print b
