# =========================================================
# 🐍 OOP PRACTICE SET
# =========================================================


# =========================================================
# 📌 Q1–Q10 BASIC
# =========================================================
print("\n--- Q1–Q10 ---")

class Student:
    school = "ABC"

    def __init__(self, name="Default"):
        self.name = name

    def greet(self):
        print("Hello", self.name)

    @staticmethod
    def static_demo():
        print("Static Method")

s1 = Student("Shrii")
s2 = Student("Rahul")

print(s1)                # Q2 object
s1.greet()               # Q3 method
Student.static_demo()    # Q10 static
print(s1.name)           # Q5 instance variable
print(Student.school)    # Q7 class variable


# =========================================================
# 📌 Q11–Q20 INTERMEDIATE
# =========================================================
print("\n--- Q11–Q20 ---")

class Math:
    def add(self, a, b):
        return a + b

    @staticmethod
    def add_static(a, b):
        return a + b

m = Math()
print(m.add(2, 3))             # Q11
print(Math.add_static(2, 3))   # Q12


class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

r = Rectangle(5, 4)
print(r.area())                # Q14


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)           # Q18


# =========================================================
# 📌 Q21–Q30 ADVANCED
# =========================================================
print("\n--- Q21–Q30 ---")

class Calc:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

c = Calc()
print(c.add(5, 2), c.sub(5, 2))   # Q21


class Demo:
    def __init__(self):
        self.show()

    def show(self):
        print("Constructor calling method")

Demo()   # Q22


class Nested:
    def __init__(self):
        self.obj = Inner()

class Inner:
    def show(self):
        print("Inner class")

n = Nested()
n.obj.show()   # Q29


class Outer:
    class Inner:
        def show(self):
            print("Inner inside Outer")

Outer.Inner().show()   # Q30


# =========================================================
# 📌 Q31–Q40 EXPERT
# =========================================================
print("\n--- Q31–Q40 ---")

class Demo2:
    count = 0

    def __init__(self):
        Demo2.count += 1

    @staticmethod
    def add(a, b):
        return a + b

d1 = Demo2()
d2 = Demo2()

print(Demo2.count)           # Q32
print(Demo2.add(2, 3))       # Q31


class Student2:
    def __init__(self, n, a):
        self.name = n
        self.age = a

s = Student2("A", 20)
print(s.name, s.age)         # Q33


class Dynamic:
    pass

d = Dynamic()
d.x = 10
print(d.x)                   # Q34

del d.x                      # Q35

print(hasattr(d, "x"))       # Q36
print(getattr(d, "x", "Not Found"))  # Q37

setattr(d, "y", 20)
print(d.y)                   # Q38


class Test:
    x = 10

del Test.x                   # Q39


class Final:
    a = 1

f = Final()
print(f.__dict__)            # Q40


# =========================================================
# 🎯 END
# =========================================================