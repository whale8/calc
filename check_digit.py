import numpy as np
import math # for log10
#import pandas as pd

def Round(value, digit):
	whole_size = len(str(value))-1				#全体の桁
	print(whole_size)
	int_size = int(math.log10(value) + 1)	#整数部の桁

	if(int_size >= digit):					#整数部が桁越え
		return digit-int_size
	elif(whole_size >= digit):				#全体では桁越え
		return digit-int_size
	else:									#桁揃え必要なし
		return digit


np_data = np.array([2718, 0.518])

#(a)
a = np_data[0] - np_data[1]
#(b)
b = np_data[0] + np_data[1]
#(c)
c = np_data[0] / np_data[1]
#(d)
d = np_data[0] * np_data[1]

solutions = np.array([a, b, c, d])

for solution in solutions:
	solution = np.round(solution, Round(solution, 4))
	print(solution)

e = 0.001111011
e = np.round(e, Round(e, 4))
print(e)
