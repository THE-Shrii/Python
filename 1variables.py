# =========================================================
# 🐍 PYTHON NOTES: VARIABLES & IDENTIFIERS
# =========================================================


# ---------------------------------------------------------
# 📌 GENERAL CONCEPT
# ---------------------------------------------------------
# Variable:
# A variable is a container used to store data in memory

# Identifier:
# Identifier is the name given to a variable, function, or class


# =========================================================
# 📌 1. VARIABLES
# =========================================================

# Syntax:
# variable_name = value


# ---------------------------------------------------------
# 💻 Examples of Variables
# ---------------------------------------------------------

name = "Shrii"     # String data type
age = 20           # Integer data type
height = 5.8       # Float data type
is_student = True  # Boolean data type

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


# ---------------------------------------------------------
# 🔄 Changing Value (Dynamic Nature)
# ---------------------------------------------------------
# Definition:
# Python allows changing the value and type of a variable anytime

x = 10
print("Initial x:", x)

x = 20   # Value updated
print("Updated x:", x)


# ---------------------------------------------------------
# 📊 Multiple Assignment
# ---------------------------------------------------------
# Definition:
# Assign multiple values to multiple variables in a single line

a, b, c = 1, 2, 3
print("Multiple values:", a, b, c)


# ---------------------------------------------------------
# ♻️ Same Value to Multiple Variables
# ---------------------------------------------------------
# Definition:
# Assign the same value to multiple variables

p = q = r = 100
print("Same value:", p, q, r)


# =========================================================
# 📌 2. IDENTIFIERS
# =========================================================

# Definition:
# Identifier is the name used to identify a variable/function/class

student_name = "Shrii"   # 'student_name' is identifier


# ---------------------------------------------------------
# ✅ Rules for Identifiers
# ---------------------------------------------------------
# 1. Can contain letters, digits, underscore (_)
# 2. Must start with letter or underscore
# 3. Cannot use keywords
# 4. Cannot contain special symbols like @, -, etc.


# ---------------------------------------------------------
# ✅ Valid Identifiers
# ---------------------------------------------------------

name = "Shrii"
_age = 20
total_marks = 95
name1 = "Python"

print(name, _age, total_marks, name1)


# ---------------------------------------------------------
# ❌ Invalid Identifiers
# ---------------------------------------------------------

# 1name = "Shrii"     # ❌ starts with number
# my-name = "Hello"   # ❌ hyphen not allowed
# class = 10          # ❌ keyword not allowed


# ---------------------------------------------------------
# 🔤 Case Sensitivity
# ---------------------------------------------------------
# Definition:
# Python is case-sensitive → lowercase and uppercase are different

name = "Shrii"
Name = "Different"

print("Lowercase:", name)
print("Uppercase:", Name)


# ---------------------------------------------------------
# 🚫 Keywords in Python
# ---------------------------------------------------------
# Definition:
# Keywords are reserved words with special meaning in Python

import keyword
print("Python Keywords:")
print(keyword.kwlist)


# =========================================================
# 🆚 VARIABLE vs IDENTIFIER
# =========================================================

# Variable → stores data/value
# Identifier → name of that variable

x = 10   # x is identifier, 10 is stored value


# =========================================================
# 🧪 PRACTICE SECTION
# =========================================================

# Create variables and print them
course = "Python"
marks = 90

print("Course:", course)
print("Marks:", marks)


# =========================================================
# 🎯 END OF NOTES
# =========================================================