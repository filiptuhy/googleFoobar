"""
Please Pass the Coded Messages
==============================

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) l = [3, 1, 4, 1]
Output:
    (int) 4311

Inputs:
    (int list) l = [3, 1, 4, 1, 5, 9]
Output:
    (int) 94311
"""
def answer(l):
	x = l.count(0)
	for o in range(x):
		l.remove(0)
#one digit list
	if len(l) ==1:
		if l[0]%3 == 0:
			return l[0]
		else:
			return 0
#more than one digit list			
	k = sorted(l,reverse=True)
	remainder = sum(l)%3
	if remainder == 0:
		return  int(''.join(str(e) for e in sorted(l,reverse=True)))
	else:
		if l.count(0) == len(l)-1:
			return 0
		# when removing exact digit
		if remainder in l:
			l.remove(remainder)
			return  int(''.join(str(e) for e in sorted(l,reverse=True)))
		else:
			#when I need to remove more digits(or one digits that sums up)
			for coun in range(len(k)):
				if (sum(k)-k[coun])%3 == 0:
					k[coun] = 0
					y = k.count(0)
					for o in range(y):
						k.remove(0)
					for p in range(x):
						k.append(0)
					return   int(''.join(str(e) for e in k))
				elif k[coun] <3:
					k[coun] = 0
		return 0
			
print answer([9,3,1,1,0,0])	
"""
print answer([3,1,4,1,5,9,2])
print answer([4])
print answer([3])
print answer([3, 1, 4, 1]) #4311 
print answer([3, 1, 4, 1, 5, 9]) #94311
print answer([3,1,4,1,1,1]) #4311
print answer([9,9,3,2,2]) #933
"""								  	
		
