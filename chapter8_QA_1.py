#8_1

def chop(t):
	del t[0],t[-1]
	return None
	
def middle(t):
	t1 = t[1:-1]
	return t1

test = [1,2,3,4,5,6,7]

ans1 = chop(test)
print (ans1)
print (test)

ans2 = middle(test)
print (ans2)
	
	
