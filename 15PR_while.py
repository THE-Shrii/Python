# ================= BASIC (1–10) =================

# Q1. Print numbers 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
# Explanation:
# Step 1: i starts from 1
# Step 2: loop runs until i <= 5
# Step 3: increment i each time
# Output: 1 2 3 4 5


# Q2. Print even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
# Explanation:
# checks condition inside loop
# Output: 2 4 6 8 10


# Q3. Print sum of first 5 numbers
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total)
# Explanation:
# adds numbers one by one
# Output: 15


# Q4. Print numbers in reverse (5 to 1)
i = 5
while i >= 1:
    print(i)
    i -= 1
# Output: 5 4 3 2 1


# Q5. Count digits in number
num = 1234
count = 0
while num > 0:
    num //= 10
    count += 1
print(count)
# Explanation:
# removes last digit each step
# Output: 4


# ================= LOGIC (11–20) =================

# Q6. Reverse a number
num = 123
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print(rev)
# Output: 321


# Q7. Check palindrome number
num = 121
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

if temp == rev:
    print("Palindrome")
# Output: Palindrome


# Q8. Find factorial
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(fact)
# Output: 120


# Q9. Print multiplication table of 3
i = 1
while i <= 10:
    print(3 * i)
    i += 1
# Output: 3 6 9 ... 30


# Q10. Sum of digits
num = 123
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)
# Output: 6


# ================= INTERMEDIATE (21–30) =================

# Q11. Guessing loop (fixed)
secret = 5
guess = 0
while guess != secret:
    guess = int(input("Guess number: "))
print("Correct")
# Explanation:
# loop runs until guess matches


# Q12. Infinite loop (break)
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1
# Output: 1 2 3 4 5


# Q13. Skip numbers using continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5


# Q14. Print squares
i = 1
while i <= 5:
    print(i*i)
    i += 1
# Output: 1 4 9 16 25


# Q15. Count vowels
s = "hello"
i = 0
count = 0
while i < len(s):
    if s[i] in "aeiou":
        count += 1
    i += 1
print(count)
# Output: 2


# Q16. Find largest digit
num = 583
max_d = 0
while num > 0:
    d = num % 10
    if d > max_d:
        max_d = d
    num //= 10
print(max_d)
# Output: 8


# Q17. Count occurrences of digit
num = 12233
count = 0
while num > 0:
    if num % 10 == 2:
        count += 1
    num //= 10
print(count)
# Output: 2


# Q18. Print ASCII values
i = 65
while i <= 70:
    print(chr(i))
    i += 1
# Output: A B C D E F


# Q19. Power calculation
base = 2
exp = 3
res = 1
while exp > 0:
    res *= base
    exp -= 1
print(res)
# Output: 8


# Q20. Count numbers divisible by 3
i = 1
count = 0
while i <= 10:
    if i % 3 == 0:
        count += 1
    i += 1
print(count)
# Output: 3


# Q21. Sum of even numbers
i = 1
total = 0
while i <= 10:
    if i % 2 == 0:
        total += i
    i += 1
print(total)
# Output: 30


# Q22. Fibonacci series (first 5)
a, b = 0, 1
i = 1
while i <= 5:
    print(a)
    a, b = b, a + b
    i += 1
# Output: 0 1 1 2 3


# Q23. Print stars
i = 1
while i <= 3:
    print("*" * i)
    i += 1
# Output:
# *
# **
# ***


# Q24. Sum until negative
num = 1
total = 0
while num >= 0:
    num = int(input("Enter number: "))
    if num >= 0:
        total += num
print(total)
# Explanation:
# stops when negative entered


# Q25. Count digits until zero
num = 9870
count = 0
while num > 0:
    count += 1
    num //= 10
print(count)
# Output: 4


# Q26. Check Armstrong (simple)
num = 153
temp = num
sum_ = 0
while num > 0:
    d = num % 10
    sum_ += d**3
    num //= 10
print(sum_ == temp)
# Output: True


# Q27. Print odd numbers
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1
# Output: 1 3 5 7 9


# Q28. Multiplication table reverse
i = 10
while i >= 1:
    print(5*i)
    i -= 1
# Output: 50 45 ... 5


# Q29. Check prime
num = 7
i = 2
is_prime = True
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
print(is_prime)
# Output: True


# Q30. Final loop condition
i = 0
while i < 3:
    print(i)
    i += 1
# Output: 0 1 2










# ================= ADVANCED (31–40) =================

# Q31. Print numbers divisible by 5 between 1–50
i = 1
while i <= 50:
    if i % 5 == 0:
        print(i)
    i += 1
# Explanation:
# checks each number, prints only multiples of 5
# Output: 5 10 15 20 25 30 35 40 45 50


# Q32. Count digits divisible by 2 in a number
num = 246135
count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        count += 1
    num //= 10
print(count)
# Explanation:
# checks each digit for even condition
# Output: 3


# Q33. Reverse string using while
s = "hello"
i = len(s) - 1
rev = ""
while i >= 0:
    rev += s[i]
    i -= 1
print(rev)
# Output: olleh


# Q34. Print sum of odd digits
num = 12345
total = 0
while num > 0:
    d = num % 10
    if d % 2 != 0:
        total += d
    num //= 10
print(total)
# Output: 1+3+5 = 9


# Q35. Check if number contains digit 5
num = 12345
found = False
while num > 0:
    if num % 10 == 5:
        found = True
        break
    num //= 10
print(found)
# Output: True


# Q36. Print pattern (reverse triangle)
i = 5
while i >= 1:
    print("*" * i)
    i -= 1
# Output:
# *****
# ****
# ***
# **
# *


# Q37. Count number of zeros in number
num = 10020
count = 0
while num > 0:
    if num % 10 == 0:
        count += 1
    num //= 10
print(count)
# Output: 3


# Q38. Product of digits
num = 123
prod = 1
while num > 0:
    prod *= num % 10
    num //= 10
print(prod)
# Output: 6


# Q39. Find smallest digit
num = 7392
small = 9
while num > 0:
    d = num % 10
    if d < small:
        small = d
    num //= 10
print(small)
# Output: 2


# Q40. Count numbers greater than 10 in list
lst = [5, 12, 7, 20]
i = 0
count = 0
while i < len(lst):
    if lst[i] > 10:
        count += 1
    i += 1
print(count)
# Output: 2


# ================= LOGIC + PATTERN (41–50) =================

# Q41. Print numbers until 0 appears
lst = [1,2,3,0,5]
i = 0
while i < len(lst):
    if lst[i] == 0:
        break
    print(lst[i])
    i += 1
# Output: 1 2 3


# Q42. Count vowels in string
s = "education"
i = 0
count = 0
while i < len(s):
    if s[i] in "aeiou":
        count += 1
    i += 1
print(count)
# Output: 5


# Q43. Print ASCII values of characters
s = "ABC"
i = 0
while i < len(s):
    print(ord(s[i]))
    i += 1
# Output: 65 66 67


# Q44. Remove digits from number (print only odd digits)
num = 123456
while num > 0:
    d = num % 10
    if d % 2 != 0:
        print(d)
    num //= 10
# Output: 5 3 1


# Q45. Count repeated elements in list
lst = [1,1,2,3,3]
i = 0
count = 0
while i < len(lst)-1:
    if lst[i] == lst[i+1]:
        count += 1
    i += 1
print(count)
# Output: 2


# Q46. Check if string has uppercase
s = "Hello"
i = 0
found = False
while i < len(s):
    if s[i].isupper():
        found = True
        break
    i += 1
print(found)
# Output: True


# Q47. Sum of numbers in list
lst = [1,2,3,4]
i = 0
total = 0
while i < len(lst):
    total += lst[i]
    i += 1
print(total)
# Output: 10


# Q48. Find max in list
lst = [5,8,2,9]
i = 0
max_val = lst[0]
while i < len(lst):
    if lst[i] > max_val:
        max_val = lst[i]
    i += 1
print(max_val)
# Output: 9


# Q49. Count words in string
s = "hello world python"
i = 0
count = 1
while i < len(s):
    if s[i] == " ":
        count += 1
    i += 1
print(count)
# Output: 3


# Q50. Final challenge: sum of squares
i = 1
total = 0
while i <= 5:
    total += i*i
    i += 1
print(total)
# Explanation:
# 1^2 + 2^2 + 3^2 + 4^2 + 5^2
# Output: 55