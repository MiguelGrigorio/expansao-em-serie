from main import todes
import matplotlib.pyplot as plt
import numpy as np
import math

Pxs = []
Pys = []

for i in range(0, len(todes)):
	Pxs.append(todes[i][0])
	Pys.append(todes[i][1])


#		  n = 5		 n = 10		 n = 30
Px_1 = [Pxs[0:20], Pxs[20:40], Pxs[40:60]]
Py_1 = [Pys[0:20], Pys[20:40], Pys[40:60]]

Px_2 = [Pxs[60:80], Pxs[80:100], Pxs[100:120]]
Py_2 = [Pys[60:80], Pys[80:100], Pys[100:120]]

Px_3 = [Pxs[120:140], Pxs[140:160], Pxs[160:180]]
Py_3 = [Pys[120:140], Pys[140:160], Pys[160:180]]

def eq(pt):
	if pt == 1:
		plt.plot(Px_1[0], Py_1[0], label = "n = 5") 
		plt.plot(Px_1[1], Py_1[1], label = "n = 10") 
		plt.plot(Px_1[2], Py_1[2], label = "n = 30") 
		plt.plot(Px_1[0], np.sin(Px_1[0]), label = "sen(x)", linestyle="-.") 
	elif pt == 2:
		plt.plot(Px_2[0], Py_2[0], label = "n = 5") 
		plt.plot(Px_2[1], Py_2[1], label = "n = 10") 
		plt.plot(Px_2[2], Py_2[2], label = "n = 30") 
		plt.plot(Px_2[0], np.cos(Px_2[0]), label = "cos(x)", linestyle="-.") 
	else:
		plt.plot(Px_3[0], Py_3[0], label = "n = 5") 
		plt.plot(Px_3[1], Py_3[1], label = "n = 10") 
		plt.plot(Px_3[2], Py_3[2], label = "n = 30") 
		plt.plot(Px_3[0], np.multiply(Px_3[0], np.float_power(math.e, (np.multiply(-2, Px_3[0])))), label = "x.e^-2x", linestyle="-.")
		# plt.xlim(0,0.55)
		# plt.ylim(-0.05, 0.25)

eq(3)
plt.legend()
plt.show()
