#Employee Hourly rate

print "Enter Hours:"
hour = int(raw_input())
print "Enter Rate:"
rate = int(raw_input())
if hour > 40:
	temp = hour - 40
	sum1 = (temp * 1.5) * rate
	sum = (40 * rate) + sum1
	print sum
else:
	sum = hour * rate
	print sum