"""

Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. You and your team of henchmen has been assigned to repair the solar panels, but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!). 

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  So answer([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). The final products may be very large, so give the answer as a string representation of the number.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) xs = [2, 0, 2, 2, 0]
Output:
    (string) "8"

Inputs:
    (int list) xs = [-2, -3, 4, -5]
Output:
    (string) "60"
"""
def product(lizzt):
	res = 1
	for n in lizzt:
		if n !=0:
			res *=n
	return res
	
def answer(lizt):
	if len(lizt)-1 == lizt.count(0):
		return str(max(lizt))
	if len(lizt) == 1:
		return str(lizt[0])
# if there are only zeroes
	if lizt.count(0) == len(lizt):
		return 0 
	minList = sorted(lizt)
	negativeCount = 0
	for n in lizt:
		if n < 0:
			negativeCount +=1
# if there is even number of negative numbers
	if negativeCount %2 == 0:
		return str(product(minList))
		
# if all numbers are negative and logicaly there has to be odd number of them
	if max(minList) <0:
			minList.remove(max(minList))
			return str(product(minList))

# other case( positive number, or positive and odd numbr of negative numbers
#I find the largest negative number and remove it
	for i in range(len(minList)):
			if minList[i] < 0 and minList[i+1] >=0:
				minList[i] = 0 
				break
	return str(product(minList))

print answer([0,-2,0,0,0])
print answer([0,-1,-2,-3])
print answer([-100])
print answer([-1,-2,-3,-4,100])
print answer([-1,-2,-3,-4])
print answer([1,2,3,3,-5,-2,-3])
print answer([-1,-2,-5])
print answer([0,0,0,0,0,0,0])
print answer([0,0,0,0,0,-5,10])
print answer([10,-5])
print answer([2, 0, 2, 2, 0])
print answer([-2, -3, 4, -5])
