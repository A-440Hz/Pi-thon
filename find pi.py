import numpy as np
import matplotlib.pyplot as plt

def pi_thon(i):
	'''calculates pi from the equation pi^2/6 = 1/1^2 + 1/2^2 + ... where i is the number of terms'''
	ins = 0
	n = 1
	xplot = []
	yplot = []
	if i <= 0:
		return "enter an integer greater than 0"

	while  i > 0:
		#iteratively calculates the sum as n increases
		ins = ins + (1/(n*n))
		val = np.sqrt(6 * ins)
		xplot.append(n)
		yplot.append(val)


		n = n + 1
		i = i - 1

	piplot = []
	while n > 1:
		piplot.append(np.pi)
		n = n - 1    
    
	plt.plot(xplot, yplot, 'g--', xplot, piplot, 'r--')
	plt.axis([100, 9999, 3.14, 3.142])
	plt.show()
	return val

pi_thon(9999)
