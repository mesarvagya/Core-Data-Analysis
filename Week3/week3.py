import numpy as np
import matplotlib.pyplot as plt
def linear_reg(filename, col1, col2, precision):
	y,x = np.loadtxt(filename, delimiter="\t", usecols=(col1,col2), unpack=True)
	std_x, std_y = np.std(x),np.std(y)
	mean_x, mean_y = np.mean(x), np.mean(y)
	rho = round(np.sum((y-mean_y)*(x-mean_x)/len(y))/(std_x*std_y), precision)
	a = round(rho * std_y / std_x, precision)
	b = round(mean_y - a * mean_x, precision)
	xranges = np.linspace(min(x),max(x),1000)
	yvalues = a * xranges + b
	# print xranges, yvalues
	plt.plot(x,y,'r.',xranges,yvalues)
	plt.axis([min(x)-0.5,max(x)+0.5,min(y)-0.5,max(y)+0.5])
	plt.title("Scatter Plot and Linear Regression Line")
	plt.show()
	return "The Value of a is %s b is %s and determinacy coeffecient is %s" %(a, b, round(rho**2,precision))

print linear_reg("dataset_389_1.txt",col1=2, col2=3, precision=6)
