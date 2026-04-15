
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
# Output: In range