"""
The Grandest Staircase Of Them All
==================================

With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER. 

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options. 

Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31
 
But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!
"""
#too slow
def answer(n):
	if n == 3:
		return 1
	if n == 4:
		return 2
	else:
		memo = {3:[[2,1]],4:[[3,1]]}
		for i in range(5,n+1):
			currentList = []
			for j in range(1,i):
				if j > i-j:
					currentList.append([j,i-j])
			memo[i] = currentList
		for i in range(4,n+1):
			for el in memo[i]:
				for inEl in memo[el[0]]:
					if el[1] not in inEl:
						insertEl = inEl+[el[1]]
						finishedEl = sorted(insertEl,reverse=True)
						if sum(finishedEl) == i:
							if finishedEl not in memo[i]:
								memo[i].append(finishedEl)
	return len(memo[n])
	
print answer(7)
print answer(9)
