#!/usr/bin/env python3

import math
import random
import signal

operations = 0
secs = int(input("secs = "))

def is_prime(n):
	prime_flag = 0
	if n > 1:
		for i in range(2, int(math.sqrt(n)) + 1):
			if (n % i == 0):
				prime_flag = 1
				break
		if (prime_flag == 0):
			return "Yes"
		else:
			return "No"
	else:
		return "No"

def handler(signum, frame):
	raise Exception("Time Limit Exceeded")

def run():
	global operations
	while True:
		a = random.uniform(0.0,10.0)
		b = random.uniform(0.0,10.0)
		print(f"{operations}: {a} + {b} = {a+b}")
		operations += 1
		print(f"{operations}: {a} - {b} = {a-b}")
		operations += 1
		print(f"{operations}: {a} * {b} = {a*b}")
		operations += 1
		print(f"{operations}: {a} / {b} = {a/b}")
		operations += 1

signal.signal(signal.SIGALRM, handler)
signal.alarm(int(secs))
try:
	run()
except Exception as exc: 
	print(exc)
print("Benchmark over!!")
print(f"Total operations: {operations}")
print(f"Time limit: {secs} seconds")
print(f"Operations/Second: {operations/secs}")
