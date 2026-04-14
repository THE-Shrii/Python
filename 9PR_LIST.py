# 1. Create a list of 5 numbers
nums = [1, 2, 3, 4, 5]  # correct

# 2. Print first element
# print(nums[0])  # 1

# 3. Print last element
# print(nums[-1])  # 5

# 4. Change second element to 10
nums[1] = 10  # [1, 10, 3, 4, 5]

# 5. Add 100 to list
nums.append(100)  # [1, 10, 3, 4, 5, 100]

# 6. Remove 3 from list
nums.remove(3)  # [1, 10, 4, 5, 100]

# 7. Length of list
# print(len(nums))  # 5

# 8. Check if 10 exists
# print(10 in nums)  # True

# 9. Find sum of list
# print(sum(nums))  # 120

# 10. Find max value
# print(max(nums))  # 100

# 11. Find min value
# print(min(nums))  # 1

# 12. Sort list ascending
nums.sort()  # sorted order

# 13. Sort descending
nums.sort(reverse=True)

# 14. Reverse list
nums.reverse()

# 15. Copy list
copy_nums = nums.copy()

# 16. Clear list
temp = [1,2,3]
temp.clear()  # []

# 17. Insert element at index
nums.insert(1, 999)

# 18. Count occurrences
# print(nums.count(10))

# 19. Get index of element
# print(nums.index(10))

# 20. Extend list
nums.extend([7, 8, 9])

# 21. Slice list first 3 elements
# print(nums[:3])

# 22. Slice last 3 elements
# print(nums[-3:])

# 23. Step slicing
# print(nums[::2])

# 24. Reverse slicing
# print(nums[::-1])

# 25. Create empty list
empty = []

# 26. List of strings
colors = ["red", "green", "blue"]

# 27. Change string in list
colors[1] = "yellow"

# 28. Append new color
colors.append("purple")

# 29. Remove element
colors.remove("red")

# 30. Print list
# print(colors)

# 31. List with mixed data types
mix = [1, "hello", 3.5, True]

# 32. Nested list
nested = [1, [2, 3], 4]

# 33. Access nested element
# print(nested[1][0])  # 2

# 34. Multiply list
# print([1,2] * 3)  # [1,2,1,2,1,2]

# 35. Check empty list
# print(len([]) == 0)

# 36. Replace multiple values
nums[0:2] = [50, 60]

# 37. Delete element by index
del nums[0]

# 38. Delete slice
del nums[0:2]

# 39. Loop list
# for i in nums:
#     print(i)

# 40. Loop with index
# for i in range(len(nums)):
#     print(nums[i])

# 41. List comprehension basic
sq = [x*x for x in range(5)]

# 42. Even numbers
evens = [x for x in range(10) if x % 2 == 0]

# 43. Odd numbers
odds = [x for x in range(10) if x % 2 != 0]

# 44. Double values
double = [x*2 for x in nums]

# 45. Filter greater than 5
greater = [x for x in nums if x > 5]

# 46. Convert list to string
words = ["Hi", "Python"]
# print(" ".join(words))

# 47. Convert string to list
# print(list("hello"))

# 48. Swap two elements
nums[0], nums[1] = nums[1], nums[0]

# 49. Copy using slicing
copy2 = nums[:]

# 50. Final print
# print(nums)










# 1. Create a tuple
t = (1, 2, 3)

# 2. Print tuple
# print(t)  # (1, 2, 3)

# 3. Print first element
# print(t[0])  # 1

# 4. Print last element
# print(t[-1])  # 3

# 5. Find length
# print(len(t))  # 3

# 6. Check type
# print(type(t))  # <class 'tuple'>

# 7. Tuple with strings
colors = ("red", "green", "blue")

# 8. Access element
# print(colors[1])  # green

# 9. Loop tuple
# for i in colors:
#     print(i)

# 10. Loop with index
# for i in range(len(colors)):
#     print(colors[i])

# 11. Tuple unpacking
a, b, c = colors

# 12. Print unpacked values
# print(a, b, c)

# 13. Single element tuple
t1 = (10,)

# 14. Check type
# print(type(t1))  # tuple

# 15. Tuple without comma (not tuple)
t2 = (10)
# print(type(t2))  # int

# 16. Count occurrences
t = (1, 2, 2, 3)
# print(t.count(2))  # 2

# 17. Find index
# print(t.index(3))  # 3

# 18. Join tuples
t3 = (1, 2)
t4 = (3, 4)
t5 = t3 + t4

# 19. Print joined tuple
# print(t5)  # (1,2,3,4)

# 20. Multiply tuple
# print(t3 * 2)  # (1,2,1,2)

# 21. Check value in tuple
# print(2 in t3)  # True

# 22. Check not in
# print(5 not in t3)  # True

# 23. Slice tuple
# print(t5[1:3])

# 24. Reverse tuple
# print(t5[::-1])

# 25. Convert tuple to list
lst = list(t3)

# 26. Modify list (since tuple is immutable)
lst[0] = 99

# 27. Convert back to tuple
t3 = tuple(lst)

# 28. Print updated tuple
# print(t3)

# 29. Nested tuple
nt = (1, (2, 3), 4)

# 30. Access nested element
# print(nt[1][1])  # 3









# List to store all students (each student is a tuple)
students = []

# Adding students (name, roll_no, marks)
students.append(("Amit", 101, 85))
students.append(("Rahul", 102, 92))
students.append(("Sneha", 103, 78))
students.append(("Priya", 104, 88))

# Print all students
print("===== STUDENT LIST =====")

for student in students:
    name = student[0]
    roll = student[1]
    marks = student[2]

    print("Name:", name)
    print("Roll No:", roll)
    print("Marks:", marks)
    print("-------------------")

# Find topper
topper = students[0]

for student in students:
    if student[2] > topper[2]:
        topper = student

print("\n===== TOPPER =====")
print("Name:", topper[0])
print("Roll No:", topper[1])
print("Marks:", topper[2])









import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 to 10: "))

if guess == number:
    print("Correct! 🎉")
elif guess > number:
    print("Too high 📈, correct number was", number)
else:
    print("Too low 📉, correct number was", number)




name = input("Enter name: ")
attendance = input("Are you present? (yes/no): ")

if attendance == "yes":
    print(name, "is Present ✅")
else:
    print(name, "is Absent ❌")










password = input("Enter password: ")

if password == "python123":
    print("Access Granted 🔓")
else:
    print("Access Denied 🔒")



student = ("Amit", 101, 85)

print("Name:", student[0])
print("Roll:", student[1])
print("Marks:", student[2])



students = []

students.append(input("Enter student 1 name: "))
students.append(input("Enter student 2 name: "))
students.append(input("Enter student 3 name: "))

print("Student List:", students)

print("First Student:", students[0])
print("Last Student:", students[-1])



a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+ - * /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")




num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")



marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade A+ 🌟")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail ❌")



username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful ✅")
else:
    print("Invalid Login ❌")



item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

total = item1 + item2 + item3

print("Total Bill:", total)

if total > 1000:
    print("You got discount offer 🎁")
else:
    print("No discount")





import random

number = random.randint(1, 10)

guess = int(input("Guess a number between 1 to 10: "))

if guess == number:
    print("Correct! 🎉")
elif guess > number:
    print("Too high 📈, correct number was", number)
else:
    print("Too low 📉, correct number was", number)