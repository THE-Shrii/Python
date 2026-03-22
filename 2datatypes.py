# =========================================================
# 🐍 PYTHON COMPLETE DATA TYPES
# =========================================================


# ---------------------------------------------------------
# 📌 DATA TYPE (GENERAL DEFINITION)
# ---------------------------------------------------------
# A data type defines the type of value a variable can store


# ---------------------------------------------------------
# 🔢 1. NUMERIC TYPES
# ---------------------------------------------------------
# Definition:
# Numeric data types are used to store numbers

a = 10          # int → stores whole numbers
b = 3.14        # float → stores decimal numbers
c = 2 + 3j      # complex → stores complex numbers

print("INT:", a, type(a))
print("FLOAT:", b, type(b))
print("COMPLEX:", c, type(c))


# ---------------------------------------------------------
# 🔤 2. STRING (str)
# ---------------------------------------------------------
# Definition:
# String is used to store sequence of characters (text)

name = "Shrii"
multi_line = """This is
multi-line string"""

print("String:", name)
print("Length:", len(name))
print("Upper:", name.upper())
print("Slice:", name[0:3])


# ---------------------------------------------------------
# 📋 3. LIST (Mutable, Ordered)
# ---------------------------------------------------------
# Definition:
# List is an ordered and mutable collection of elements

my_list = [1, 2, 3, "Python"]

print("List:", my_list)

# Operations
my_list.append(100)   # add element
my_list.remove(2)     # remove element
print("Updated List:", my_list)


# ---------------------------------------------------------
# 📦 4. TUPLE (Immutable, Ordered)
# ---------------------------------------------------------
# Definition:
# Tuple is an ordered but immutable collection

my_tuple = (1, 2, 3)

print("Tuple:", my_tuple)

# my_tuple[0] = 10 ❌ Not allowed (immutable)


# ---------------------------------------------------------
# 🔗 5. SET (Unordered, Unique)
# ---------------------------------------------------------
# Definition:
# Set is an unordered collection of unique elements

my_set = {1, 2, 3, 3, 4}

print("Set:", my_set)   # duplicates removed automatically

# Operations
my_set.add(10)
my_set.remove(2)
print("Updated Set:", my_set)


# ---------------------------------------------------------
# 🗂️ 6. DICTIONARY (Key-Value Pair)
# ---------------------------------------------------------
# Definition:
# Dictionary stores data in key-value pairs

student = {
    "name": "Shrii",
    "age": 20,
    "marks": 90
}

print("Dictionary:", student)
print("Name:", student["name"])

# Add / Update
student["age"] = 21
student["city"] = "Bhilai"

print("Updated Dictionary:", student)


# ---------------------------------------------------------
# ✔ 7. BOOLEAN (True/False)
# ---------------------------------------------------------
# Definition:
# Boolean data type represents logical values: True or False

is_logged_in = True
print("Boolean:", is_logged_in)

# Boolean operations
print(10 > 5)   # True
print(5 > 10)   # False


# ---------------------------------------------------------
# ❌ 8. NONE TYPE
# ---------------------------------------------------------
# Definition:
# None represents absence of value (no data)

x = None
print("None value:", x)
print(type(x))


# ---------------------------------------------------------
# 🔄 TYPE CASTING (Conversion)
# ---------------------------------------------------------
# Definition:
# Type casting is converting one data type into another

a = "10"
b = int(a)     # string → int
c = float(a)   # string → float

print("Converted Int:", b)
print("Converted Float:", c)


# ---------------------------------------------------------
# 🔍 TYPE CHECKING
# ---------------------------------------------------------
# Definition:
# type() function is used to check data type

print(type(10))
print(type("Hello"))
print(type([1,2,3]))


# ---------------------------------------------------------
# 🧪 NESTED DATA TYPES
# ---------------------------------------------------------
# Definition:
# Nested data types are data structures inside another

data = {
    "name": "Shrii",
    "skills": ["Python", "React"],
    "marks": (90, 95),
    "active": True
}

print("Nested Data:", data)


# =========================================================
# 🎯 END OF COMPLETE DATA TYPES
# =========================================================