# 01 Count Even Digits
# Given an integer N, count how many of its decimal digits are even (0, 2, 4, 6, 8). Ignore a negative sign. Treat 0 as a one-digit number. Use arithmetic operations and a loop.
'''n = int(input("Enter a number: "))
count = 0
n = abs(n)
if n == 0:
    count = 1
else:
    for i in range(len(str(n))):
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
print(count)'''

# 02 Check Strong Number
# A number is strong when the sum of the factorials of its digits equals the original number. For this task, use non-negative integers. Print Strong Number or Not Strong Number.
'''n = int(input("Enter a number: "))
temp = n
total = 0
while n > 0:
    digit = n % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    total += fact
    n = n // 10
if total == temp:
    print("Strong")
else:
    print("Not Strong")'''

# 03 Find Digital Root
# Repeatedly add the digits of a non-negative integer until only one digit remains. Print that final digit. Solve it using loops rather than a built-in shortcut.
'''n = int(input("Enter a number: "))
while n >= 10:
    total = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        total += digit
    n = total
print(n)'''

# 04 Check Happy Number
# For a positive integer N, repeatedly replace it with the sum of the squares of its digits. If it reaches 1, print Happy Number; if it enters a repeating cycle, print Not Happy Number.
'''n = int(input("Enter a number: "))
s = set()
while n != 1 and n not in s:
    s.add(n)
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10
    n = total
if n == 1:
    print("Happy Number")
else:
    print("Not Happy Number")'''

# 05 Find the Next Palindrome Number
# Given a non-negative integer N, find the smallest integer strictly greater than N whose digits read the same forward and backward. Do not use string reversal to check the palindrome.
'''n = int(input("Enter a number: "))
num = n + 1
while True:
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    if num == rev:
        print(num)
        break
    num += 1'''

   