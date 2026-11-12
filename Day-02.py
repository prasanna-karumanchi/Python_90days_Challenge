# 01 Check Whether a Number Is Prime [Easy]
# Given an integer n, print whether it is prime. A prime number is greater than 1 and has exactly two positive divisors.
'''n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            print("Not Prime")
            break
    else:
        print("Prime")'''

# 02 Count the Factors of a Number [Easy]
# Given a positive integer n, count how many positive integers divide n exactly.
'''n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print("Factors of a number:", count)'''

# 03 Print Prime Numbers in a Range [Medium]
# Given integers L and R (1 <= L <= R), print all prime numbers between L and R, inclusive, in ascending order. If none exist, print None.
'''L = int(input("Enter Starting Number: "))
R = int(input("Enter ending Number: "))
found = 0
for num in range(L, R + 1):
    count = 0
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(num, end = " ")
            found = True
if found == False:
    print("None")'''

# 04 Find GCD and LCM [Medium]
# Given two positive integers a and b, find their greatest common divisor (GCD) and least common multiple (LCM).
'''a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = a
y = b
while b != 0:
    r = a % b
    a = b
    b = r
gcd = a
lcm = (x * y) // gcd
print("GCD:", gcd)
print("LCM:", lcm)'''

# 05 Prime Factorization [Challenge]
# Given an integer n >= 2, print its prime factors in ascending order, repeating each factor as many times as it divides n.
'''n = int(input("Enter a number: "))
i = 2
while n > 1:
    if n % i == 0:
        print(i, end = " ")
        n = n // i
    else:
        i = i + 1'''