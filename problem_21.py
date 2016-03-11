table = {}
amicable_numbers = []
UPPER_BOUND = 10000 # given by the problem

def sum_of_divisors(x):
	result = 0
	for num in range (1,x):
		if x%num == 0:
			result += num
	return result

def compute_sum_of_divisors(): # pre-computing, should make things more efficient
	for num in range(1,UPPER_BOUND):
		table[num] = sum_of_divisors(num)

def solve_problem():
	compute_sum_of_divisors()
	for num in table.values():
		try:
			if num == 1: continue # skip primes
			if (num == table[table[num]] and num != table[num]): # i.e. the logical condition for an amicable number
				amicable_numbers.append(num)
				amicable_numbers.append(table[num])
		except KeyError:
			continue

def clean_array(arr):
	return list(set(arr)) # remove duplicates

solve_problem()
print sum(clean_array(amicable_numbers))