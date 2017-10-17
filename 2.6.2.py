import numpy as np

np_data = np.array([2718, 0.518])
formulas = []

#(a)
formulas.append('2718 - 0.518 =')
a = np_data[0] - np_data[1]
#(b)
formulas.append('2718 + 0.518 =')
b = np_data[0] + np_data[1]
#(c)
formulas.append('2718 / 0.518 =')
c = np_data[0] / np_data[1]
#(d)
formulas.append('2718 * 0.518 =')
d = np_data[0] * np_data[1]

solutions = np.array([a, b, c, d])

print("------------誤差無し-----------")
for formula, solution in zip(formulas, solutions):
	print(formula, solution)

print("------------誤差あり-----------")
for formula, solution in zip(formulas, solutions):
	print(formula, "{0:8.4g}".format(solution))	#これでいいのか？
