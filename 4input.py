# =========================================================
# 🐍 PYTHON INPUT FUNCTION
# =========================================================


# ---------------------------------------------------------
# 📌 DEFINITION
# ---------------------------------------------------------
# input() function is used to take input from the user
# It always returns the value in STRING format by default


# ---------------------------------------------------------
# 💻 BASIC EXAMPLE
# ---------------------------------------------------------

name = input("Enter your name: ")
print("Hello", name)

# 👉 Output:
# Enter your name: Shrii
# Hello Shrii


# ---------------------------------------------------------
# ⚠️ IMPORTANT POINT
# ---------------------------------------------------------
# input() always takes value as STRING

age = input("Enter your age: ")
print(type(age))   # Output will be <class 'str'>


# ---------------------------------------------------------
# 🔄 TYPE CASTING (VERY IMPORTANT)
# ---------------------------------------------------------
# To use numbers, we must convert input into int or float

age = int(input("Enter your age: "))
print("Age:", age)
print(type(age))   # <class 'int'>


# ---------------------------------------------------------
# 🔢 MULTIPLE INPUTS
# ---------------------------------------------------------
# Taking multiple inputs in one line

a, b = input("Enter two numbers: ").split()

print("A:", a)
print("B:", b)


# ---------------------------------------------------------
# 🔢 MULTIPLE INPUTS WITH TYPE CASTING
# ---------------------------------------------------------

a, b = map(int, input("Enter two numbers: ").split())

print("Sum:", a + b)


# 👉 Example Input:
# Enter two numbers: 10 20
# Output:
# Sum: 30


# ---------------------------------------------------------
# 🧪 PRACTICE EXAMPLE 1
# ---------------------------------------------------------
# Take name and age and print message

name = input("Enter name: ")
age = int(input("Enter age: "))

print(name, "is", age, "years old")


# ---------------------------------------------------------
# 🧪 PRACTICE EXAMPLE 2
# ---------------------------------------------------------
# Take two numbers and print their sum

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Sum is:", x + y)


# ---------------------------------------------------------
# 🎯 KEY POINTS TO REMEMBER
# ---------------------------------------------------------
# 1. input() always returns string
# 2. Use int() or float() for numbers
# 3. Use split() for multiple inputs
# 4. Use map() for multiple type conversion


# =========================================================
# 🎯 END OF NOTES
# =========================================================