# =========================================================
# 🐍 PYTHON OPERATORS
# =========================================================


# ---------------------------------------------------------
# 📌 OPERATOR (GENERAL DEFINITION)
# ---------------------------------------------------------
# An operator is a symbol that performs an operation
# on one or more operands (values/variables)

print(5 + 3)  # '+' is operator, 5 & 3 are operands


# ---------------------------------------------------------
# 🔢 1. ARITHMETIC OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to perform mathematical calculations

a = 10
b = 3

print(a + b)  # Addition → 13
print(a - b)  # Subtraction → 7
print(a * b)  # Multiplication → 30
print(a / b)  # Division → 3.33
print(a % b)  # Modulus → 1


# ---------------------------------------------------------
# 📝 2. ASSIGNMENT OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to assign values to variables

x = 5
x += 3   # x = x + 3
print(x) # 8


# ---------------------------------------------------------
# 🔍 3. COMPARISON OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to compare values and return True/False

a = 10
b = 5

print(a == b)  # False
print(a > b)   # True


# ---------------------------------------------------------
# 🧠 4. LOGICAL OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to combine conditions

x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False


# ---------------------------------------------------------
# ⚙️ 5. BITWISE OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators that work on binary (bit-level) values

a = 5   # 0101
b = 3   # 0011

print(a & b)  # AND → 1
print(a | b)  # OR → 7


# ---------------------------------------------------------
# 📦 6. MEMBERSHIP OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to check if a value exists in a sequence

my_list = [1, 2, 3]

print(2 in my_list)      # True
print(5 not in my_list)  # True


# ---------------------------------------------------------
# 🆔 7. IDENTITY OPERATORS
# ---------------------------------------------------------
# Definition:
# Operators used to compare memory location of objects

a = [1, 2]
b = a
c = [1, 2]

print(a is b)      # True (same memory)
print(a is c)      # False (different memory)


# =========================================================
# 🎯 END
# =========================================================