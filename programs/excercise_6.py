from pylab import plot, show, legend
from random import normalvariate
alpha=[0,0.8,0.98]
for a in alpha:
    series=[0]
    for i in range(200):
        series.append(a*series[i]+normalvariate(0,1))
    plot(series,label=a)
    series=[]
legend()
show()
