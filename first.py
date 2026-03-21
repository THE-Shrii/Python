# =========================================================
# 🐍 PYTHON DAY 1 - COMPLETE BASICS (BY SHRII)
# =========================================================

# ---------------------------------------------------------
# 📌 WHAT IS PYTHON?
# Python is a high-level, interpreted programming language.
# It is easy to learn and widely used in web dev, AI, data science, etc.
# ---------------------------------------------------------

# ---------------------------------------------------------
# 👨‍💻 YOUR FIRST PROGRAM
# ---------------------------------------------------------

# This is a comment (Python ignores this line)
print("Hey Shrii")   # print() displays output

# OUTPUT:
# Hey Shrii


# ---------------------------------------------------------
# 🧠 COMMENTS IN PYTHON
# ---------------------------------------------------------

# Single-line comment

"""
Multi-line comment
Used for documentation
"""


# ---------------------------------------------------------
# 📦 VARIABLES (STORING DATA)
# ---------------------------------------------------------

name = "Shrii"   # String (text)
age = 20         # Integer (whole number)
height = 5.8     # Float (decimal number)
is_student = True  # Boolean (True/False)

# Printing variables
print("Name:", name)
print("Age:", age)


# ---------------------------------------------------------
# 🔢 DATA TYPES IN PYTHON
# ---------------------------------------------------------

a = 10        # int
b = 3.14      # float
c = "Hello"   # string
d = True      # boolean

print(type(a))  # shows data type


# ---------------------------------------------------------
# 🧮 BASIC OPERATIONS
# ---------------------------------------------------------

x = 5
y = 3

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)


# ---------------------------------------------------------
# 📥 INPUT FROM USER
# ---------------------------------------------------------

# Takes input as string by default
user_name = input("Enter your name: ")

# Output using variable
print("Hello", user_name)


# ---------------------------------------------------------
# 🔄 TYPE CASTING
# ---------------------------------------------------------

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sum_result = num1 + num2
print("Sum is:", sum_result)


# ---------------------------------------------------------
# ⚙️ HOW PYTHON WORKS
# ---------------------------------------------------------

# Python uses an INTERPRETER
# Code → Interpreter → Output
# No compilation needed like C/C++


# ---------------------------------------------------------
# 📜 HISTORY OF PYTHON
# ---------------------------------------------------------

# Created by Guido van Rossum in 1991
# Name inspired from "Monty Python"


# ---------------------------------------------------------
# ✅ FEATURES / ADVANTAGES
# ---------------------------------------------------------

# 1. Easy syntax (beginner friendly)
# 2. Platform independent
# 3. Large community
# 4. Huge libraries (AI, ML, Web)
# 5. Fast development


# ---------------------------------------------------------
# ❌ DRAWBACKS
# ---------------------------------------------------------

# 1. Slower than C/C++
# 2. High memory usage
# 3. Not best for mobile apps


# ---------------------------------------------------------
# 🚀 FINAL EXAMPLE (COMBINED)
# ---------------------------------------------------------

# Taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Processing
next_age = age + 1

# Output
print("Hello", name)
print("Next year your age will be:", next_age)


# =========================================================
# 🎯 END OF DAY 1
# =========================================================