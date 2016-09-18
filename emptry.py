#Employee Hourly rate

print "Enter Hours:"
hours = raw_input()
print "Enter Rate:"
rates = raw_input()
try:
	hour=int(hours)
	rate=float(rates)
		if hour > 40:
			temp = hour - 40
			sum1 = (temp * 1.5) * rate
			sum = (40 * rate) + sum1
			print sum
		else:
			sum = hour * rate
			print sum
except:
	print "Error, Please Enter Numeric Input"
