#!/usr/bin/env python3

## RECUSIVE ALWAYS HAVE THIS 2 STEPS:

## STEP 1. The Base Case -- simple condition that 
## stops function calling itself forever

## STEP 2. The Recursive -- the way to call the func
## again with a 'smaller' version of the original problem

# 1. The Countdown without While Loop
def countdown(n):
    if n <= 0:              ### Base Case: stop at 0
        print("Blast off!")
    else:
        print(n)
        countdown(n - 1)    # Recursive call again with smal-
                            ## ler number


# 2. Factorial(n!)
## This is a closest math equivalent to determinant code:
## 5! is 5 x 4 x 3 x 2 x 1

def factorial(n):
    if n == 1:
        return 1            ### Base Case: 1! is just !

    # Recursive Step: n! = n * (n-1)!
    return n * factorial(n - 1)


# 3. Summing a List
## This recursion 'shrinks' data, like mtx into minor.

def sum_list(nums):
    if not nums:            ### Base Case: Sum of an []
        return 0
    
    # Recursive Step: Take the first number + sum of rest
    return nums[0] + sum_list(nums[1:])