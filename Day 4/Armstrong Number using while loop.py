#! /usr/bin/env python

numRange = range(1042000, 702648265 + 1)

while True:
	for x in numRange:
		length = len(str(x))
		Sum = 0
		temp = x
		
		while temp > 0:
			n = temp % 10
			Sum += n ** length
			temp //= 10
			if Sum == temp:
				break
		
		if Sum == x:
			print("The first armstrong number is >>> ", x)
			break
	break
			
	

	