# Project Euler
# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

###############################################
# WORKING VERSION v02
###############################################

upper = 1000
sum = 0

# check for factors
for i in range(3,upper):
    if (i % 3) == 0:
     sum=sum+i
    elif (i % 5) == 0:
     sum=sum+i

print(sum," is a sum")


