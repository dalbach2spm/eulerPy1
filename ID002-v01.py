# Project Euler
# https://projecteuler.net/problem=1
# Even Fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

###############################################
#  VERSION v01
###############################################

maxElementOfFibonacci = 4000000
Min2Fib = 0
Min1Fib = 1
currentFib = 2
sum = 0

while currentFib <= maxElementOfFibonacci:
   # check if this element is even
   if (currentFib % 2) == 0:
     sum = sum + currentFib
   
   # calculate next element of Fibonacci sequence
   Min2Fib = Min1Fib
   Min1Fib = currentFib
   currentFib = Min1Fib + Min2Fib

# output the result
print(sum," is a sum")

