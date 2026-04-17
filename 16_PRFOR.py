
# ================= BASIC (1–10) =================

# Q1. Print numbers from 1 to 5
for i in range(1, 6):
    print(i)
# Explanation:
# range(1,6) → 1,2,3,4,5 (last number excluded)
# loop prints each value
# Output: 1 2 3 4 5


# Q2. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
# Explanation:
# checks each number for even condition
# Output: 2 4 6 8 10


# Q3. Print sum of numbers 1 to 5
total = 0
for i in range(1, 6):
    total += i
print(total)
# Explanation:
# adds numbers one by one
# Output: 15


# Q4. Print reverse numbers (5 to 1)
for i in range(5, 0, -1):
    print(i)
# Explanation:
# start=5, stop=1, step=-1
# Output: 5 4 3 2 1


# Q5. Print multiplication table of 3
for i in range(1, 11):
    print(3 * i)
# Output: 3 6 9 ... 30


# Q6. Loop through string
for ch in "hello":
    print(ch)
# Explanation:
# iterates character by character
# Output: h e l l o


# Q7. Loop through list
lst = [1,2,3]
for i in lst:
    print(i)
# Output: 1 2 3


# Q8. Count elements in list
lst = [10,20,30]
count = 0
for _ in lst:
    count += 1
print(count)
# Output: 3


# Q9. Find max in list
lst = [5,8,2]
max_val = lst[0]
for i in lst:
    if i > max_val:
        max_val = i
print(max_val)
# Output: 8


# Q10. Print squares
for i in range(1, 6):
    print(i*i)
# Output: 1 4 9 16 25


# ================= INTERMEDIATE (11–20) =================

# Q11. Sum of even numbers
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total += i
print(total)
# Output: 30


# Q12. Count vowels in string
s = "hello"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)
# Output: 2


# Q13. Reverse string
s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
# Output: nohtyp


# Q14. Print ASCII values
for ch in "ABC":
    print(ord(ch))
# Output: 65 66 67


# Q15. Find common elements
a = [1,2,3]
b = [2,3,4]
for i in a:
    if i in b:
        print(i)
# Output: 2 3


# Q16. Print pattern
for i in range(1, 4):
    print("*" * i)
# Output:
# *
# **
# ***


# Q17. Nested loop (table)
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
# Output:
# 1 1
# 1 2
# 2 1
# 2 2


# Q18. Break example
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output: 1 2


# Q19. Continue example
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5


# Q20. Sum of digits
num = 123
total = 0
for d in str(num):
    total += int(d)
print(total)
# Output: 6


# ================= ADVANCED (21–30) =================

# Q21. Factorial
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)
# Output: 120


# Q22. Check palindrome
s = "madam"
if s == s[::-1]:
    print("Palindrome")
# Output: Palindrome


# Q23. Fibonacci series
a, b = 0, 1
for _ in range(5):
    print(a)
    a, b = b, a+b
# Output: 0 1 1 2 3


# Q24. Count digits
num = 1234
count = 0
for _ in str(num):
    count += 1
print(count)
# Output: 4


# Q25. Find smallest number
lst = [5,2,8]
small = lst[0]
for i in lst:
    if i < small:
        small = i
print(small)
# Output: 2


# Q26. Check prime
num = 7
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)
# Output: True


# Q27. Sum of list
lst = [1,2,3]
print(sum(lst))
# Output: 6


# Q28. Remove duplicates
lst = [1,2,2,3]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)
# Output: [1,2,3]


# Q29. Count words
s = "hello world python"
print(len(s.split()))
# Output: 3


# Q30. Final challenge: sum of squares
total = 0
for i in range(1, 6):
    total += i*i
print(total)
# Output: 55