from random import uniform

def binomial(n,p):
	
	count=0
	for i in range(n):
	    if uniform(0,1)<p:
	        count=count+1
	return count

a=[binomial(10,0.8) for i in range(20)]

print a
avg=0
for i in range(len(a)):
    avg=avg+a[i]
print avg

print avg/len(a)