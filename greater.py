print "Enter Two Numbers"
input1 = raw_input()
input2 = raw_input()
x=int(input1)
y=int(input2)
if x<y:
	print str(x)+" is less than "+str(y)
elif x>y:
	print str(x)+" is greater than "+str(y)
else:
	print str(x)+" and "+str(y)+" are equal"

	