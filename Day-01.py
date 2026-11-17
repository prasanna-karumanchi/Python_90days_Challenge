# 01 Reverse an Integer | Easy 
# Read an integer and print its digits in reverse order. Do not convert it to a string or use slicing. Keep the minus sign for negative inputs. Leading zeros disappear.
'''num = int(input("Enter a number:"))
reverse = 0
if num < 0:
    sign = -1
    num = -num
else:
    sign = 1
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
reverse = reverse * sign
print("Reversed Number:", reverse)'''

# 02 Check Numeric Palindrome | Easy 
# Determine whether a non-negative integer reads the same forwards and backwards. Use arithmetic rather than string reversal. Treat negative numbers as not palindromes.
'''num = int(input("Enter digits: "))
if num < 0:
    print("Not Palindrome")
else:
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")'''

# 03 Sum of Digits | Easy-Medium 
# Calculate the sum of the decimal digits of an integer using a loop. Ignore the minus sign for negative values.
'''num = int(input("Enter numbers: "))
num = abs(num)
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of numbers: ", sum)'''

# 04 Check Armstrong Number | Medium 
# An Armstrong number equals the sum of its digits, each raised to the power of the total number of digits. Check any non-negative integer, not just three-digit numbers.
'''num = int(input("Enter numbers: "))
original = num
digits = len(str(num))
total = 0
while num > 0:
    digit = num % 10
    power = digit ** digits
    total = total + power
    num = num // 10
if total == original:
    print("Armstrong Numner")
else:
    print("Not Armstrong Numner")'''

# 05 Find the Next Prime | Challenge
# Given an integer N, find the smallest prime strictly greater than N. A prime is greater than 1 and has exactly two positive divisors. For efficiency, check divisors only up to the square root.
'''num = int(input("Enter a number: "))
num += 1
while True:
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print("Next Prime:", num)
        break
    num += 1'''