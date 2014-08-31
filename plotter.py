import matplotlib.pyplot as plt
import numpy as NP

def plotBeliefStates(fc,trueId,meanfc,strname,iteration):
	print iteration
	x, y = zip(*fc)
	plt.clf()
	plt.plot(x, y, 'rx', trueId[1], trueId[2], 'bs', meanfc[1], meanfc[2], 'g^')
	#plt.show()
	plt.savefig(strname+`iteration`)

def plotRobotsLocation(xarray,yarray,g,numiteration):
	plt.clf()
	iterationarray = list(range(1, numiteration+1, 1))
	#goalarray = NP.ones(numiteration)*g
	plt.plot(iterationarray,abs(NP.subtract(xarray,yarray)),'r-',iterationarray,abs(NP.subtract(xarray,g)),'b-',iterationarray,abs(NP.subtract(yarray,g)),'g-')
	plt.savefig('locations'+`numiteration`)