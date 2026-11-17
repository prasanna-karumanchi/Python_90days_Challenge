# 01 Reverse an Integer
# Write a program that reverses the digits of an integer using arithmetic operations only. Preserve the negative sign and remove leading zeros in the reversed result.
'''n = int(input("Enter a number: "))
rev = 0
if n < 1:
    sign = -1
    n = -n
else:
    sign = 1
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
        rev = rev * sign
    print(rev)'''

# 02 Check Whether a Number Is Prime
# Given an integer N, print whether it is prime. A prime is greater than 1 and has exactly two positive factors. Check divisors efficiently up to the square root of N.
'''n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")'''

# 03 Find GCD of Two Numbers
# Given two non-negative integers A and B, find their greatest common divisor using the Euclidean algorithm. If one number is zero, the GCD is the other number; GCD(0,0) is defined as 0 for this exercise.
'''a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
    gcd = a
print("GCD of 2 numbers:", gcd)'''

# 04 Generate the Fibonacci Series
# Given N, print the first N Fibonacci numbers starting from 0, 1. If N is zero, print an empty sequence. Use an iterative approach.
'''n = int(input("Enter N: "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c'''

# 05 Find the Next Palindrome Number
# Given a non-negative integer N, find the smallest integer strictly greater than N whose decimal representation reads the same forward and backward.
'''n = int(input("Enter a number: "))
n += 1
while True:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print("Next prime:", n)
        break
    n += 1'''