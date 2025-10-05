'''
def prime_check(number):
    if number > 1 and number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % number == 0:
        print (f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


inputNumber = input("please input a number\n")
prime_check(int(inputNumber))
'''

def prime_checker(number):
	is_prime = True
	for i in range(2, number):
		if number % i == 0:
			is_prime = False
			"""here has no else statement, so as long as when the number can be dividied by i, the is_prime will be false, even when it continue to finish the loop, is_prime will stay as false"""
	if is_prime:
		print("It's a prime number.")
	else:
		print("It's not a prime number.")


n = int(input()) # Check this number
prime_checker(number=n)