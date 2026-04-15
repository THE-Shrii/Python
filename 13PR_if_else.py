# 1. Check if number is positive
num = 5
if num > 0:
    print("Positive")
# Output: Positive

# 2. Check if number is negative or positive
num = -3
if num >= 0:
    print("Positive")
else:
    print("Negative")
# Output: Negative

# 3. Check even or odd
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# Output: Even

# 4. Check voting eligibility
age = 18
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# 5. Find greater of two numbers
a, b = 10, 20
if a > b:
    print(a)
else:
    print(b)
# Output: 20

# 6. Find greatest of three numbers
a,b,c = 10,20,15
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)
# Output: 20

# 7. Check number is zero
num = 0
if num == 0:
    print("Zero")

# 8. Check divisible by 5
num = 25
if num % 5 == 0:
    print("Divisible")

# 9. Check multiple conditions
x = 15
if x > 10 and x < 20:
    print("Between 10 and 20")

# 10. Check leap year
year = 2024
if (year%4==0 and year%100!=0) or year%400==0:
    print("Leap Year")

# 11. Grade system
marks = 85
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
# Output: B

# 12. Check vowel
ch = 'a'
if ch in "aeiou":
    print("Vowel")

# 13. Check alphabet or not
ch = 'A'
if ch.isalpha():
    print("Alphabet")

# 14. Check uppercase
if ch.isupper():
    print("Uppercase")

# 15. Check lowercase
if ch.islower():
    print("Lowercase")

# 16. Check number is multiple of 3 and 7
num = 21
if num%3==0 and num%7==0:
    print("Yes")

# 17. Nested if
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive Even")

# 18. Check pass/fail
marks = 40
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# 19. Check temperature
temp = 30
if temp > 25:
    print("Hot")
else:
    print("Cold")

# 20. Check string length
s = "hello"
if len(s) > 3:
    print("Long")

# 21. Compare strings
a = "hi"
b = "hi"
if a == b:
    print("Equal")

# 22. Check empty string
s = ""
if not s:
    print("Empty")

# 23. Check list empty
lst = []
if not lst:
    print("Empty list")

# 24. Check if key exists
d = {"a":1}
if "a" in d:
    print("Exists")

# 25. Check element in set
s = {1,2,3}
if 2 in s:
    print("Found")

# 26. Ternary operator
a = 10
print("Even" if a%2==0 else "Odd")

# 27. Check password length
pwd = "12345"
if len(pwd) >= 6:
    print("Strong")
else:
    print("Weak")

# 28. Check greater than 100
num = 150
if num > 100:
    print("Big")

# 29. Check divisible by 2 or 3
num = 9
if num%2==0 or num%3==0:
    print("Yes")

# 30. Nested condition
x = 50
if x > 10:
    if x < 100:
        print("Between")

# 31. Check age group
age = 10
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")

# 32. Check number range
num = 7
if 1 <= num <= 10:
    print("In range")

# 33. Check special character
ch = "@"
if not ch.isalnum():
    print("Special")

# 34. Check multiple elif
x = 2
if x==1:
    print("One")
elif x==2:
    print("Two")
else:
    print("Other")

# 35. Check divisible by 10
num = 50
if num%10==0:
    print("Yes")

# 36. Compare 3 strings
a,b,c = "a","b","c"
if a<b and a<c:
    print("a is smallest")

# 37. Check number > 0 and < 50
num = 25
if 0 < num < 50:
    print("Valid")

# 38. Check list length
lst = [1,2,3]
if len(lst) >= 3:
    print("OK")

# 39. Check dictionary empty
d = {}
if not d:
    print("Empty dict")

# 40. Check number is square
n = 16
if int(n**0.5)**2 == n:
    print("Perfect square")

# 41. Check palindrome string
s = "madam"
if s == s[::-1]:
    print("Palindrome")

# 42. Check largest digit
num = 123
if max(str(num)) == '3':
    print("3 is largest")

# 43. Check char is digit
ch = '5'
if ch.isdigit():
    print("Digit")

# 44. Check number divisible by 4
num = 8
if num%4==0:
    print("Yes")

# 45. Check if string starts with 'a'
s = "apple"
if s.startswith("a"):
    print("Yes")

# 46. Check ends with 'z'
s = "quiz"
if s.endswith("z"):
    print("Yes")

# 47. Check multiple conditions
x = 20
if x > 10 and x % 2 == 0:
    print("Valid")

# 48. Check list contains even
lst = [1,3,5,6]
if any(i%2==0 for i in lst):
    print("Even present")

# 49. Check all numbers positive
lst = [1,2,3]
if all(i>0 for i in lst):
    print("All positive")

# 50. Check if two numbers equal
a,b = 5,5
if a == b:
    print("Equal")