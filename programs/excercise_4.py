from random import uniform

count = 0
counter=[]
for i in range(10):
	if uniform(0,1)<0.5:
	    count=count+1
	else:
	    count=0
	counter.append(count)   
	print counter
if max(counter)>2:
	print 1
else:
	print 0