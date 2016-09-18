inp = raw_input('Enter Fahrenheit temp\n')
try:
	fahr = float(inp)
	cel = (fahr - 32.0) * 5.0 / 9.0
	print cel
except:
	print 'Please Enter a Number'
	