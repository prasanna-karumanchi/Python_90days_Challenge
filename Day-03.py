# 01 Generate the Fibonacci Series [Easy]
# Given a non-negative integer N, print the first N Fibonacci numbers. The series begins with 0 and 1; every later term is the sum of the previous two. For N = 0, print an empty sequence.
'''n = int(input("Enter N: "))
a = 0
b = 1
for i in range(n):
    print(a, end = " ")
    c = a + b
    a = b
    b = c'''

# 02 Sum of Squares [Easy]
# Given a positive integer N, calculate 1² + 2² + ... + N². Write a loop-based solution first.
'''n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i * i
print(total)'''

# 03 Generate an Arithmetic Progression [Medium]
# Given the first term A, common difference D, and positive number of terms N, print the first N terms of the arithmetic progression. D may be negative or zero.
'''a = int(input("Enter A: "))
d = int(input("Enter D: "))
n = int(input("Enter N: "))
current = a
for i in range(1, n + 1):
    print(current, end = " ")
    current = current + d'''

# 04 Find the Nth Fibonacci Number [Medium]
# Given a non-negative integer N, return the Fibonacci number at zero-based index N. F(0) = 0 and F(1) = 1.
'''n = int(input("Enter N: "))
a = 0
b = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(b)'''

# 05 Find the Missing Term in an AP [Challenge]
# An arithmetic progression originally contains at least four terms. Exactly one internal term (not the first or last) has been removed. You are given the remaining terms in their original order; find the missing value. The common difference is a non-zero integer.
'''lst = list(map(int, input("Enter numbers:").split(",")))
first = lst[0]
last = lst[-1]
total = len(lst)
d = (last - first) // len(lst)
for i in range(len(lst) - 1):
    if lst[i + 1] - lst[i] != d:
        missing = lst[i] + d
        print(missing)
        break'''
