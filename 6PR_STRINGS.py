# 1
x = "Hello"
print(x)
# Output: Hello
# Explanation: String print hota hai

# 2
x = 'Hello'
print(x)
# Output: Hello
# Explanation: Single quotes bhi valid

# 3
x = """Hello"""
print(x)
# Output: Hello
# Explanation: Triple quotes multi-line ke liye use hote hain

# 4
x = "Hello"
print(type(x))
# Output: <class 'str'>
# Explanation: String type

# 5
x = "Python"
print(len(x))
# Output: 6
# Explanation: Length count

# 6
x = "Python"
print(x[0])
# Output: P
# Explanation: Index 0 = first char

# 7
x = "Python"
print(x[-1])
# Output: n
# Explanation: -1 = last char

# 8
x = "Python"
print(x[1:4])
# Output: yth
# Explanation: Slice (start:end-1)

# 9
x = "Python"
print(x[:3])
# Output: Pyt
# Explanation: Start se index 2 tak

# 10
x = "Python"
print(x[3:])
# Output: hon
# Explanation: Index 3 se end tak

# 11
x = "Python"
print(x[::-1])
# Output: nohtyP
# Explanation: Reverse string

# 12
x = "Hello"
print("H" in x)
# Output: True
# Explanation: Membership check (case-sensitive)

# 13
x = "Hello"
print("h" in x)
# Output: False
# Explanation: Case sensitive

# 14
x = "Hello"
print(x.upper())
# Output: HELLO
# Explanation: Uppercase

# 15
x = "HELLO"
print(x.lower())
# Output: hello
# Explanation: Lowercase

# 16
x = "Hello"
print(x.strip())
# Output: Hello
# Explanation: No extra spaces

# 17
x = " Hello "
print(x.strip())
# Output: Hello
# Explanation: Spaces remove

# 18
x = "Hello World"
print(x.replace("World", "Python"))
# Output: Hello Python
# Explanation: Replace word

# 19
x = "Hello World"
print(x.split())
# Output: ['Hello', 'World']
# Explanation: Space se split

# 20
x = "a,b,c"
print(x.split(","))
# Output: ['a', 'b', 'c']
# Explanation: Custom split

# 21
x = "Hello"
y = "World"
print(x + y)
# Output: HelloWorld
# Explanation: Concatenation

# 22
x = "Hello"
y = "World"
print(x + " " + y)
# Output: Hello World
# Explanation: Space manually add

# 23
name = "Shrii"
print(f"Hello {name}")
# Output: Hello Shrii
# Explanation: f-string formatting

# 24
age = 20
print(f"Age is {age}")
# Output: Age is 20
# Explanation: Variable embed

# 25
x = "Python"
print(x.count("o"))
# Output: 1
# Explanation: Count occurrences

# 26
x = "Python"
print(x.find("t"))
# Output: 2
# Explanation: Index return

# 27
x = "Python"
print(x.index("t"))
# Output: 2
# Explanation: Same as find (error if not found)

# 28
x = "Python"
print(x.startswith("Py"))
# Output: True
# Explanation: Prefix check

# 29
x = "Python"
print(x.endswith("on"))
# Output: True
# Explanation: Suffix check

# 30
x = "hello world"
print(x.title())
# Output: Hello World
# Explanation: First letter capital

# 31
x = "hello"
print(x.capitalize())
# Output: Hello
# Explanation: First letter capital only

# 32
x = "HELLO"
print(x.swapcase())
# Output: hello
# Explanation: Case reverse

# 33
x = "123"
print(x.isdigit())
# Output: True
# Explanation: Only digits

# 34
x = "abc"
print(x.isalpha())
# Output: True
# Explanation: Only letters

# 35
x = "abc123"
print(x.isalnum())
# Output: True
# Explanation: Letters + numbers

# 36
x = "Python"
print(x.replace("o", "0"))
# Output: Pyth0n
# Explanation: Replace char

# 37
x = "  Python  "
print(len(x.strip()))
# Output: 6
# Explanation: Spaces remove then count

# 38
x = "Python"
print(x[::2])
# Output: Pto
# Explanation: Step slicing

# 39
x = "Python"
print(x[1::2])
# Output: yhn
# Explanation: Alternate chars

# 40
x = "Python"
print(x[-3:])
# Output: hon
# Explanation: Last 3 chars

# 41
x = "Python"
print(x[:-1])
# Output: Pytho
# Explanation: Last char remove

# 42
x = "Python"
print("".join(x))
# Output: Python
# Explanation: Join characters

# 43
x = ["a", "b", "c"]
print("".join(x))
# Output: abc
# Explanation: List → string

# 44
x = "Python"
print(list(x))
# Output: ['P', 'y', 't', 'h', 'o', 'n']
# Explanation: String → list

# 45
x = "Hello"
print(x * 3)
# Output: HelloHelloHello
# Explanation: Repeat string

# 46
x = "Hello"
print(x == "Hello")
# Output: True
# Explanation: Exact match

# 47
x = "Hello"
print(x == "hello")
# Output: False
# Explanation: Case-sensitive

# 48
x = "Hello"
print(x.lower() == "hello")
# Output: True
# Explanation: Case normalize

# 49
x = "Hello123"
print(x.isalpha())
# Output: False
# Explanation: Contains digits

# 50
x = "   "
print(x.strip() == "")
# Output: True
# Explanation: Only spaces → empty