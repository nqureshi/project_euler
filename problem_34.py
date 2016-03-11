UPPER_BOUND = 2540160
# you can work this out using deduction; essentially, 9! * digits(n) < n 
# becomes true once you get to 8-digit numbers, so you get an upper bound of 9,999,999
# and from there you can deduce that 9! * 7 = 2540160 is the next upper bound

def factorial(x):
	if x == 0: return 1;
	else:
		result = 1;
		for num in range (1,x):
			result += result * num
		return result

def factorial_sum(x):
	arr = [int(a) for a in str(x)];
	output = 0;
	for number in arr:
		output += factorial(number);
	return output

def find_the_answer(x):
	for num in range(x,UPPER_BOUND):
		if num != factorial_sum(num):
			x += 1
		else:
			print num
			find_the_answer(num+1)
	print "Done"
	return None

find_the_answer(3)