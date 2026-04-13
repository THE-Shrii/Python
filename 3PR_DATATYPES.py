# 1
x = 10
print(type(x))
# Output: <class 'int'>
# Explanation: Integer type

# 2
x = 10.5
print(type(x))
# Output: <class 'float'>
# Explanation: Decimal value → float

# 3
x = "Hello"
print(type(x))
# Output: <class 'str'>
# Explanation: String type

# 4
x = True
print(type(x))
# Output: <class 'bool'>
# Explanation: Boolean type

# 5
x = 1j
print(type(x))
# Output: <class 'complex'>
# Explanation: Complex number (real + imaginary)

# 6
x = [1, 2, 3]
print(type(x))
# Output: <class 'list'>
# Explanation: List (mutable collection)

# 7
x = (1, 2, 3)
print(type(x))
# Output: <class 'tuple'>
# Explanation: Tuple (immutable list)

# 8
x = {"a": 1, "b": 2}
print(type(x))
# Output: <class 'dict'>
# Explanation: Key-value pair

# 9
x = {1, 2, 3}
print(type(x))
# Output: <class 'set'>
# Explanation: Unique unordered values

# 10
x = None
print(type(x))
# Output: <class 'NoneType'>
# Explanation: No value assigned

# 11
x = "10"
print(type(x))
# Output: <class 'str'>
# Explanation: Number inside quotes = string

# 12
x = int("10")
print(type(x))
# Output: <class 'int'>
# Explanation: String → int conversion

# 13
x = float(5)
print(type(x))
# Output: <class 'float'>
# Explanation: int → float

# 14
x = str(10)
print(type(x))
# Output: <class 'str'>
# Explanation: int → string

# 15
x = bool(1)
print(type(x))
# Output: <class 'bool'>
# Explanation: Non-zero = True

# 16
x = [1, 2, 3]
print(x[0])
# Output: 1
# Explanation: Index 0 = first element

# 17
x = (10, 20, 30)
print(x[1])
# Output: 20
# Explanation: Indexing in tuple

# 18
x = {"name": "John"}
print(x["name"])
# Output: John
# Explanation: Dictionary key access

# 19
x = {1, 2, 3}
print(2 in x)
# Output: True
# Explanation: Membership check

# 20
x = "Python"
print(x[2])
# Output: t
# Explanation: String indexing

# 21
x = [1, 2, 3]
x.append(4)
print(x)
# Output: [1, 2, 3, 4]
# Explanation: append() new element add karta hai

# 22
x = [1, 2, 3]
x.remove(2)
print(x)
# Output: [1, 3]
# Explanation: remove() value delete karta hai

# 23
x = (1, 2, 3)
# x[0] = 10
# Output: Error
# Explanation: Tuple immutable hota hai

# 24
x = {"a": 1}
x["b"] = 2
print(x)
# Output: {'a': 1, 'b': 2}
# Explanation: New key-value add

# 25
x = {1, 2, 3}
x.add(4)
print(x)
# Output: {1, 2, 3, 4}
# Explanation: Set me element add

# 26
x = [1, 2, 3]
y = x
y.append(4)
print(x)
# Output: [1, 2, 3, 4]
# Explanation: Same reference (memory shared)

# 27
x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)
# Output: [1, 2, 3]
# Explanation: Copy me separate memory

# 28
x = "Hello"
print(len(x))
# Output: 5
# Explanation: Length count

# 29
x = [1, 2, 3]
print(len(x))
# Output: 3
# Explanation: List length

# 30
x = {"a": 1, "b": 2}
print(len(x))
# Output: 2
# Explanation: Dictionary keys count

# 31
x = set([1, 2, 2, 3])
print(x)
# Output: {1, 2, 3}
# Explanation: Duplicate remove hota hai

# 32
x = list((1, 2, 3))
print(type(x))
# Output: <class 'list'>
# Explanation: Tuple → list

# 33
x = tuple([1, 2, 3])
print(type(x))
# Output: <class 'tuple'>
# Explanation: List → tuple

# 34
x = dict(a=1, b=2)
print(x)
# Output: {'a': 1, 'b': 2}
# Explanation: Dictionary creation

# 35
x = set("abc")
print(x)
# Output: {'a', 'b', 'c'}
# Explanation: String → set (unique chars)

# 36
x = [1, 2, 3]
print(type(x) == list)
# Output: True
# Explanation: Type comparison

# 37
x = (1, 2, 3)
print(isinstance(x, tuple))
# Output: True
# Explanation: Recommended type check

# 38
x = "10"
y = 10
print(x == y)
# Output: False
# Explanation: Different types

# 39
x = [1, 2]
y = [1, 2]
print(x == y)
# Output: True
# Explanation: Values same

# 40
x = [1, 2]
y = x
print(x is y)
# Output: True
# Explanation: Same memory reference

# 41
x = [1, 2]
y = [1, 2]
print(x is y)
# Output: False
# Explanation: Different objects

# 42
x = None
print(x is None)
# Output: True
# Explanation: Best way to check None

# 43
x = [1, 2, 3]
print(4 in x)
# Output: False
# Explanation: Not present

# 44
x = {"a": 1}
print("a" in x)
# Output: True
# Explanation: Key check

# 45
x = {"a": 1}
print(1 in x)
# Output: False
# Explanation: Value check nahi hota directly

# 46
x = [1, 2, 3]
del x[1]
print(x)
# Output: [1, 3]
# Explanation: Index delete

# 47
x = [1, 2, 3]
x.clear()
print(x)
# Output: []
# Explanation: List empty

# 48
x = {"a": 1}
x.clear()
print(x)
# Output: {}
# Explanation: Dictionary empty

# 49
x = [1, 2, 3]
print(type(x[0]))
# Output: <class 'int'>
# Explanation: Element type check

# 50
x = [{"a": 1}, {"b": 2}]
print(x[1]["b"])
# Output: 2
# Explanation: Nested access (list + dict)