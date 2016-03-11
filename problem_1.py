def is_multiple(x):
	if x%3 == 0:
		return True
	elif x%5 == 0:
		return True
	else:
		return False

result = 0
for x in range (1,1000):
	if is_multiple(x) == True:
		result += x

print result # >>233168