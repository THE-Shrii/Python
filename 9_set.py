# =========================================================
# 🐍 PYTHON NOTES: SET
# =========================================================


# =========================================================
# 📌 1. WHAT IS A SET?
# =========================================================

# Definition:
# Set is an unordered, mutable collection of unique elements.

# Key Features:
# ✔ Unordered (no index)
# ✔ No duplicate values
# ✔ Mutable (can change)
# ✔ Elements must be immutable (int, string, tuple)

s = {1, 2, 3, 4}

print("Set:", s)
print("Type:", type(s))

# Output (order may vary):
# Set: {1, 2, 3, 4}
# Type: <class 'set'>


# =========================================================
# 📌 2. DUPLICATES NOT ALLOWED
# =========================================================

s = {1, 2, 2, 3, 3}

print(s)

# Output:
# {1, 2, 3}


# =========================================================
# 📌 3. EMPTY SET (IMPORTANT)
# =========================================================

s = set()   # correct
print(type(s))

# Output:
# <class 'set'>

# s = {} ❌ This creates dictionary


# =========================================================
# 📌 4. ADD ELEMENTS
# =========================================================

s = {1, 2}

s.add(3)
print(s)

# Output:
# {1, 2, 3}


# =========================================================
# 📌 5. UPDATE (MULTIPLE VALUES)
# =========================================================

s.update([4, 5])
print(s)

# Output:
# {1, 2, 3, 4, 5}


# =========================================================
# 📌 6. REMOVE ELEMENTS
# =========================================================

# remove()
s.remove(5)
print(s)

# discard()
s.discard(10)   # no error
print(s)

# pop()
print("Removed:", s.pop())  # random element
print(s)

# clear()
s.clear()
print(s)

# Output (may vary):
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# Removed: 1
# {2, 3, 4}
# set()


# =========================================================
# 📌 7. SET OPERATIONS
# =========================================================

a = {1, 2, 3}
b = {3, 4, 5}

# Union
print(a.union(b))
print(a | b)

# Intersection
print(a.intersection(b))
print(a & b)

# Difference
print(a.difference(b))
print(a - b)

# Symmetric Difference
print(a.symmetric_difference(b))
print(a ^ b)

# Output:
# {1,2,3,4,5}
# {1,2,3,4,5}
# {3}
# {3}
# {1,2}
# {1,2}
# {1,2,4,5}
# {1,2,4,5}


# =========================================================
# 📌 8. SET METHODS (ALL IMPORTANT)
# =========================================================

a = {1, 2, 3}
b = {3, 4, 5}

# union()
print(a.union(b))

# intersection()
print(a.intersection(b))

# difference()
print(a.difference(b))

# symmetric_difference()
print(a.symmetric_difference(b))

# issubset()
print({1,2}.issubset(a))

# issuperset()
print(a.issuperset({1,2}))

# isdisjoint()
print(a.isdisjoint({10,20}))

# copy()
c = a.copy()
print(c)

# Output:
# {1,2,3,4,5}
# {3}
# {1,2}
# {1,2,4,5}
# True
# True
# True
# {1,2,3}


# =========================================================
# 📌 9. LOOPING
# =========================================================

s = {1, 2, 3}

for i in s:
    print(i)

# Output:
# 1 2 3 (order may vary)


# =========================================================
# 📌 10. MEMBERSHIP
# =========================================================

print(2 in s)
print(10 not in s)

# Output:
# True
# True


# =========================================================
# 📌 11. BUILT-IN FUNCTIONS
# =========================================================

s = {5, 2, 8, 1}

print(len(s))
print(max(s))
print(min(s))
print(sum(s))

# Output:
# 4
# 8
# 1
# 16


# =========================================================
# 📌 12. SET COMPREHENSION
# =========================================================

s = {x*x for x in range(5)}
print(s)

# Output:
# {0,1,4,9,16}


# =========================================================
# 📌 13. CONVERTING SET
# =========================================================

lst = [1,2,2,3]

s = set(lst)
print(s)

lst2 = list(s)
print(lst2)

# Output:
# {1,2,3}
# [1,2,3]


# =========================================================
# 📌 14. IMPORTANT USE CASE
# =========================================================

# Remove duplicates
lst = [1,2,2,3,3]
print(list(set(lst)))

# Output:
# [1,2,3]


# =========================================================
# 📌 15. FINAL EXAM LINE
# =========================================================

print("Set = Unordered + Unique + Mutable")

# Output:
# Set = Unordered + Unique + Mutable