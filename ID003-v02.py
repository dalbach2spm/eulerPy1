# Project Euler
# https://projecteuler.net/problem=1

# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


###############################################
# WORKING VERSION v02
# v02 - find factors from highest one
# start with (number // 3) + 1
###############################################

# function to calculate if factor is prime number
def isPrimeNumber (n):
   """Function to return 
   1 - if n is prime number
   0 - if n isn't prime number"""
   nHalf = n  // 2
   for i in range(2,nHalf):
      if (n % i) == 0:
       return 0
   return 1



# definition of variables
number = 600851475143
thirdOfNumber = number // 3
largestPrimeFactor = 1

# check for factors
for i in reversed (range(thirdOfNumber)):
    if (number % i) == 0:
       # check if factor "i" is prime number
       if isPrimeNumber(i) == 1:
          largestPrimeFactor = i
          print("prime factor is: ", largestPrimeFactor)
          break


print("largest peime factor is: ", largestPrimeFactor)


