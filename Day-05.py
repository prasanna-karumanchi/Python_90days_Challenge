# 01  Number Triangle
# Given a positive integer N, print N rows. Row i must contain the numbers from 1 to i, separated by one space.
'''n = int(input("Enter a number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()'''

# 02 Floyd's Triangle
# Given N, print N rows of consecutive integers starting at 1. Row i contains exactly i numbers.
'''n = int(input("Enter a number: "))
count = 1
for i in range(1, n + 1):
    for j in range(i):
        print(count, end = " ")
        count += 1
    print()'''

# 03  Hollow Square
# Given N (N >= 2), print an N by N hollow square using * characters. The first and last rows are filled; interior rows have stars only at both ends.
'''n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()'''

# 04  Centered Star Pyramid
# Given N, print a centered pyramid of N rows. Row i has N-i leading spaces followed by 2*i-1 stars. Do not add spaces between stars.
'''n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()'''

# 05 Diamond Star Pattern
# Given N, print a symmetric diamond of 2*N-1 rows. The widest row contains 2*N-1 stars. Avoid repeating the middle row.
'''n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(2 * i + 1):
        print("*", end = " ")
    print()
for i in range(n - 2, -1, -1):
    for j in range(n - i - 1):
        print(" ", end = " ")
    for j in range(2 * i + 1 ):
        print("*", end = " ")
    print()'''