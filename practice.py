
# ================= BASIC + OUTPUT =================

# Q1. Compare integer and string
x = 5
y = "5"
print(x == y)
# Explanation:
# x is integer (5), y is string ("5")
# Python does NOT auto-convert types in comparison
# So 5 != "5"
# Output: False


# Q2. Boolean evaluation
print(bool(0), bool(""), bool("Hello"))
# Explanation:
# bool(0) → False (0 is considered False)
# bool("") → False (empty string)
# bool("Hello") → True (non-empty string)
# Output: False False True


# Q3. Division operators
a, b = 10, 3
print(a / b, a // b)
# Explanation:
# / → normal division (returns float)
# // → floor division (returns integer part)
# Output: 3.3333333333333335 3


# Q4. Data types
print(type(10), type("hi"))
# Explanation:
# type() returns the datatype of variable
# 10 → int, "hi" → string
# Output: <class 'int'> <class 'str'>


# Q5. Type casting
x = "10"
print(int(x) + 5)
# Explanation:
# "10" is string → convert using int()
# 10 + 5 = 15
# Output: 15


# ================= STRINGS =================

# Q6. String indexing
s = "Python"
print(s[1])
# Explanation:
# Index starts from 0 → P=0, y=1
# Output: y


# Q7. Negative indexing
print(s[-1])
# Explanation:
# -1 means last character → n
# Output: n


# Q8. String slicing
print(s[1:4])
# Explanation:
# starts at index 1 → y
# ends before index 4 → h
# Output: yth


# Q9. String repetition
print("Hi" * 3)
# Explanation:
# string repeats 3 times
# Output: HiHiHi


# Q10. String methods
print("hello".upper())
# Explanation:
# converts string to uppercase
# Output: HELLO


# ================= OPERATORS =================

# Q11. Operator precedence
print(2 + 3 * 4)
# Explanation:
# multiplication first → 3*4=12
# then addition → 2+12=14
# Output: 14


# Q12. Logical operator
print(True and False)
# Explanation:
# AND returns True only if both True
# Output: False


# Q13. Comparison
print(5 > 3, 5 < 2)
# Explanation:
# 5>3 → True
# 5<2 → False
# Output: True False


# ================= LIST =================

# Q14. List creation
lst = [1,2,3]
print(lst)
# Explanation:
# simple list of integers
# Output: [1, 2, 3]


# Q15. Append element
lst.append(4)
print(lst)
# Explanation:
# adds element at end
# Output: [1, 2, 3, 4]


# Q16. Insert element
lst.insert(1, 10)
print(lst)
# Explanation:
# inserts 10 at index 1
# Output: [1, 10, 2, 3, 4]


# Q17. Remove last element
print(lst.pop())
# Explanation:
# removes last element (4)
# Output: 4


# Q18. Membership
print(2 in lst)
# Explanation:
# checks if element exists
# Output: True


# Q19. List slicing
print(lst[1:3])
# Explanation:
# elements from index 1 to 2
# Output: [10, 2]


# Q20. Nested list
lst2 = [1, [2,3]]
print(lst2[1][0])
# Explanation:
# access inner list → [2,3]
# then first element → 2
# Output: 2


# ================= TUPLES =================

# Q21. Tuple creation
t = (1,2,3)
print(t)
# Explanation:
# tuple is immutable
# Output: (1, 2, 3)


# Q22. Access tuple
print(t[0])
# Explanation:
# index 0 → first element
# Output: 1


# Q23. Tuple slicing
print(t[1:])
# Explanation:
# from index 1 to end
# Output: (2, 3)


# Q24. Tuple count
t2 = (1,2,2,3)
print(t2.count(2))
# Explanation:
# counts occurrences of 2
# Output: 2


# Q25. Tuple index
print(t2.index(3))
# Explanation:
# position of 3
# Output: 3


# Q26. Tuple unpacking
a,b,c = t
print(a,b,c)
# Explanation:
# assigns values individually
# Output: 1 2 3


# Q27. Join tuple
print(t + (4,))
# Explanation:
# tuples can be concatenated
# Output: (1, 2, 3, 4)


# Q28. Repeat tuple
print(t * 2)
# Explanation:
# repeats tuple
# Output: (1, 2, 3, 1, 2, 3)


# ================= SET =================

# Q29. Set removes duplicates
s = {1,2,2,3}
print(s)
# Explanation:
# sets store unique values only
# Output: {1, 2, 3}


# Q30. Add element
s.add(4)
print(s)
# Explanation:
# adds new element
# Output: {1, 2, 3, 4}


# Q31. Set intersection
a = {1,2,3}
b = {2,3,4}
print(a & b)
# Explanation:
# common elements
# Output: {2, 3}


# ================= DICTIONARY =================

# Q32. Create dict
d = {"a":1, "b":2}
print(d)
# Output: {'a':1,'b':2}


# Q33. Access value
print(d["a"])
# Explanation:
# key "a" → value 1
# Output: 1


# Q34. Update value
d["a"] = 10
print(d)
# Explanation:
# value updated
# Output: {'a':10,'b':2}


# Q35. Add new key
d["c"] = 3
print(d)
# Output: {'a':10,'b':2,'c':3}


# Q36. Loop dictionary
for k,v in d.items():
    print(k,v)
# Explanation:
# prints key-value pairs


# ================= IF-ELSE =================

# Q37. Even or odd
x = 4
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
# Output: Even


# Q38. Nested if
x = 15
if x > 10:
    if x % 5 == 0:
        print("Valid")
# Output: Valid


# Q39. Ternary operator
x = 5
print("Even" if x%2==0 else "Odd")
# Output: Odd


# Q40. Range check
x = 7
if 1 <= x <= 10:
    print("In range")
<<<<<<< HEAD
# Output: In range




# ================= LIST + LOGIC =================

# Q41. List comprehension
lst = [i*i for i in range(5)]
print(lst)
# Explanation:
# range(5) → 0 to 4
# squares → 0,1,4,9,16
# Output: [0, 1, 4, 9, 16]


# Q42. Filter even numbers
lst = [1,2,3,4,5]
evens = [i for i in lst if i%2==0]
print(evens)
# Explanation:
# selects only numbers divisible by 2
# Output: [2, 4]


# Q43. Reverse list
lst = [1,2,3]
print(lst[::-1])
# Explanation:
# slicing with step -1 reverses list
# Output: [3, 2, 1]


# Q44. Extend list
lst1 = [1,2]
lst2 = [3,4]
lst1.extend(lst2)
print(lst1)
# Explanation:
# adds elements of lst2 into lst1
# Output: [1, 2, 3, 4]


# Q45. Remove element
lst = [1,2,3]
lst.remove(2)
print(lst)
# Explanation:
# removes value 2
# Output: [1, 3]


# ================= TUPLE ADVANCED =================

# Q46. Tuple inside tuple
t = (1,(2,3))
print(t[1][1])
# Explanation:
# inner tuple (2,3) → index 1 = 3
# Output: 3


# Q47. Convert tuple to list
t = (1,2,3)
lst = list(t)
print(lst)
# Explanation:
# conversion allows modification
# Output: [1, 2, 3]


# Q48. Single element tuple
t = (5,)
print(type(t))
# Explanation:
# comma is required
# Output: <class 'tuple'>


# Q49. Tuple unpacking with *
t = (1,2,3,4)
a,*b = t
print(a,b)
# Explanation:
# a=1, b=[2,3,4]
# Output: 1 [2, 3, 4]


# Q50. Max in tuple
t = (5,2,8)
print(max(t))
# Output: 8


# ================= SET ADVANCED =================

# Q51. Union
a = {1,2}
b = {2,3}
print(a | b)
# Explanation:
# combines unique elements
# Output: {1, 2, 3}


# Q52. Difference
print(a - b)
# Explanation:
# elements in a not in b
# Output: {1}


# Q53. Symmetric difference
print(a ^ b)
# Explanation:
# elements not common
# Output: {1, 3}


# Q54. Check subset
print({1}.issubset(a))
# Explanation:
# 1 exists in a
# Output: True


# Q55. Remove safely
a.discard(10)
# Explanation:
# no error if element not present


# ================= DICTIONARY ADVANCED =================

# Q56. get method
d = {"a":1}
print(d.get("b", 0))
# Explanation:
# returns default value if key missing
# Output: 0


# Q57. Dictionary comprehension
sq = {i:i*i for i in range(3)}
print(sq)
# Explanation:
# creates key:value pairs
# Output: {0:0,1:1,2:4}


# Q58. Keys and values
d = {"x":1,"y":2}
print(list(d.keys()), list(d.values()))
# Output: ['x','y'] [1,2]


# Q59. Merge dict
d1 = {"a":1}
d2 = {"b":2}
print({**d1, **d2})
# Output: {'a':1,'b':2}


# Q60. Pop item
d = {"a":1,"b":2}
d.pop("a")
print(d)
# Output: {'b':2}


# ================= STRING LOGIC =================

# Q61. Count characters
s = "hello"
print(s.count("l"))
# Output: 2


# Q62. Replace string
print(s.replace("l","x"))
# Output: hexxo


# Q63. Split string
print("a,b,c".split(","))
# Output: ['a','b','c']


# Q64. Join string
lst = ["a","b","c"]
print("-".join(lst))
# Output: a-b-c


# Q65. Check palindrome
s = "madam"
print(s == s[::-1])
# Output: True


# ================= BOOLEAN + OPERATORS =================

# Q66. OR operator
print(True or False)
# Output: True


# Q67. NOT operator
print(not True)
# Output: False


# Q68. Complex condition
x = 10
print(x>5 and x<20)
# Output: True


# ================= IF-ELSE ADVANCED =================

# Q69. Grade system
marks = 75
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
else:
    print("C")
# Output: B


# Q70. Multiple conditions
x = 15
if x%3==0 and x%5==0:
    print("Divisible by both")
# Output: Divisible by both


# Q71. Nested condition
x = 8
if x>5:
    if x%2==0:
        print("Even >5")
# Output: Even >5


# ================= MIXED =================

# Q72. Zip lists
a = [1,2]
b = ["a","b"]
print(list(zip(a,b)))
# Output: [(1,'a'),(2,'b')]


# Q73. Any function
print(any([0,0,1]))
# Output: True


# Q74. All function
print(all([1,2,3]))
# Output: True


# Q75. Sum of list
print(sum([1,2,3]))
# Output: 6


# Q76. Max key in dict
d = {"a":5,"b":10}
print(max(d, key=d.get))
# Output: b


# Q77. Reverse string
print("abc"[::-1])
# Output: cba


# Q78. Check digit
print("5".isdigit())
# Output: True


# Q79. Check alpha
print("abc".isalpha())
# Output: True


# Q80. Mixed condition
x = 20
if x>10 and x%2==0:
    print("Valid")
# Output: Valid


# ================= FINAL LOGIC =================

# Q81. Remove duplicates
lst = [1,2,2,3]
print(list(set(lst)))
# Output: [1,2,3]


# Q82. Frequency count
lst = [1,1,2]
d = {}
for i in lst:
    d[i] = d.get(i,0)+1
print(d)
# Output: {1:2,2:1}


# Q83. Flatten list
lst = [[1,2],[3,4]]
flat = [i for sub in lst for i in sub]
print(flat)
# Output: [1,2,3,4]


# Q84. Even numbers using set
print({i for i in range(6) if i%2==0})
# Output: {0,2,4}


# Q85. Dict from lists
k = ["a","b"]
v = [1,2]
print(dict(zip(k,v)))
# Output: {'a':1,'b':2}


# Q86. Tuple to string
t = ('a','b')
print("".join(t))
# Output: ab


# Q87. Check empty list
print(not [])
# Output: True


# Q88. Multiply list elements
lst = [1,2,3]
res = 1
for i in lst:
    res *= i
print(res)
# Output: 6


# Q89. Largest in list
print(max([3,7,2]))
# Output: 7


# Q90. Smallest in list
print(min([3,7,2]))
# Output: 2


# Q91. Square dict
print({i:i*i for i in range(4)})
# Output: {0:0,1:1,2:4,3:9}


# Q92. String length
print(len("Python"))
# Output: 6


# Q93. Check substring
print("py" in "python")
# Output: True


# Q94. Convert set to list
print(list({1,2,3}))
# Output: [1,2,3]


# Q95. Remove key safely
d = {"a":1}
d.pop("b", None)
print(d)
# Output: {'a':1}


# Q96. Check tuple
print(type((1,)))
# Output: <class 'tuple'>


# Q97. Compare lists
print([1,2]==[1,2])
# Output: True


# Q98. Compare tuples
print((1,2)<(1,3))
# Output: True


# Q99. Boolean check
print(bool([]), bool([1]))
# Output: False True


# Q100. Final mixed
lst = [1,2,3,4]
print([i for i in lst if i%2!=0])
# Output: [1,3]
=======
# Output: In range
>>>>>>> f0ba588923cf7847c28421dd3e19a892546bd759
