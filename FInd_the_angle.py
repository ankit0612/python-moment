import math

AB = float(input()) 
BC = float(input())

print("Angle will be :- "+str
	(int
		(round
			(math.degrees
				(math.atan2(AB,BC)
					)
				)
			)
		)+'\N{DEGREE SIGN}')