


def prime_checker(number):
                    # We set it to True, since we are going to check every single number that is not 1 or the checked number. If ANY of these numbers has a reminder of 0, this will set the variable to False, and we can be sure that our number is NOT a prime number
 is_prime = True    # We set the variable is_prime in the same indentation level as the for Loop to avoid Unboundlocalerror: Otherwise this variable will not be accessible outside of the for loop, and we need the variable is_prime to be available for the "If/else" statement below 
 for i in range(2,number):
            
         if number % i == 0:
             is_prime = False
                
 if is_prime: #Here is where we need to evaluate the variable is_prime to reveal if the number we are checking is prime or not. 
             print("prime")
 else:
             print("not prime")


n = int(input("Enter a number to find out if it's a prime number: "))
prime_checker(number=n)
