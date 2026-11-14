# 01 Count Digits in a Number
# Given a non-negative integer N, determine how many decimal digits it contains using a while loop. The number 0 has one digit.
'''n = int(input("Enter digits: "))
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n  = n // 10
        count += 1
print(count)'''

# 02 Reverse a Number Using While
# Given a non-negative integer N, reverse its decimal digits using arithmetic and a while loop. Print the result as an integer, so leading zeros disappear.
'''n = int(input("Enter a number: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse:", rev)'''

# 03 Check a Perfect Number
# A positive integer is perfect if the sum of its positive divisors excluding itself equals the number. Write a program to determine whether N is perfect.
'''n = int(input("Enter a number: "))
total = 0
i = 1
while i < n:
    if n % i == 0:
        total += i
    i += 1
if total == n:
    print("Perfect Number")
else:
    print("Not a perfect number")'''

# 04 Generate the Collatz Sequence
# Start with a positive integer N. If it is even, divide it by 2; if odd, replace it with 3N + 1. Repeat until reaching 1. Print the complete sequence including the starting number and 1.
'''n = int(input("Enter a number: "))
while n != 1:
    print(n, end = ",")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(1)'''

# 05 Longest Collatz Sequence up to N
# For every starting integer from 1 through N, generate its Collatz sequence. Find the starting integer whose sequence contains the most terms, counting both the start and final 1. If tied, return the smaller starting integer.
n = int(input("Enter N: "))
max_terms = 0
best_start = 1
for start in range(1, n + 1):
    num = start
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        count += 1
    if count > max_terms:
        max_terms = count
        best_start = start
print("Start =", best_start)
print("Terms =", max_terms)