# =========================================================
# 🐍 PYTHON NOTES: DICTIONARY
# =========================================================


# =========================================================
# 📌 1. WHAT IS A DICTIONARY?
# =========================================================

# Definition:
# Dictionary is an unordered (insertion-ordered in Python 3.7+),
# mutable collection of key-value pairs.

# Key Features:
# ✔ Key-Value pair
# ✔ Mutable (can change)
# ✔ Keys must be unique
# ✔ Ordered (Python 3.7+ maintains insertion order)

d = {"name": "Shrii", "age": 20}

print("Dictionary:", d)
print("Type:", type(d))

# Output:
# Dictionary: {'name': 'Shrii', 'age': 20}
# Type: <class 'dict'>


# =========================================================
# 📌 2. ACCESSING VALUES
# =========================================================

print(d["name"])       # Direct access
print(d.get("age"))    # Safe access

# Output:
# Shrii
# 20


# =========================================================
# 📌 3. ADD / UPDATE VALUES
# =========================================================

d["city"] = "Delhi"    # Add
d["age"] = 21          # Update

print(d)

# Output:
# {'name': 'Shrii', 'age': 21, 'city': 'Delhi'}


# =========================================================
# 📌 4. REMOVE ELEMENTS
# =========================================================

# pop()
d.pop("city")

# popitem()
d.popitem()

# del
d = {"a":1, "b":2}
del d["a"]

print(d)

# Output:
# {'b': 2}


# =========================================================
# 📌 5. LOOPING IN DICTIONARY
# =========================================================

d = {"x":1, "y":2}

# Keys
for k in d:
    print(k)

# Values
for v in d.values():
    print(v)

# Key + Value
for k, v in d.items():
    print(k, v)

# Output:
# x y
# 1 2
# x 1 | y 2


# =========================================================
# 📌 6. DICTIONARY METHODS (ALL IMPORTANT)
# =========================================================

d = {"a":1, "b":2}

# keys()
print(d.keys())

# values()
print(d.values())

# items()
print(d.items())

# get()
print(d.get("a"))

# update()
d.update({"c":3})
print(d)

# pop()
d.pop("c")
print(d)

# popitem()
d.popitem()
print(d)

# clear()
d.clear()
print(d)

# copy()
d = {"a":1}
d2 = d.copy()
print(d2)

# setdefault()
d.setdefault("b", 2)
print(d)

# fromkeys()
print(dict.fromkeys(["x","y"], 0))


# Output:
# dict_keys(['a', 'b'])
# dict_values([1, 2])
# dict_items([('a', 1), ('b', 2)])
# 1
# {'a': 1, 'b': 2, 'c': 3}
# {'a': 1, 'b': 2}
# {'a': 1}
# {}
# {'a': 1}
# {'a': 1, 'b': 2}
# {'x': 0, 'y': 0}


# =========================================================
# 📌 7. BUILT-IN FUNCTIONS
# =========================================================

d = {"a":10, "b":20}

print(len(d))
print(max(d))         # max key
print(min(d))         # min key
print(sum(d.values()))

# Output:
# 2
# b
# a
# 30


# =========================================================
# 📌 8. MEMBERSHIP
# =========================================================

print("a" in d)
print("z" not in d)

# Output:
# True
# True


# =========================================================
# 📌 9. NESTED DICTIONARY
# =========================================================

d = {
    "student": {
        "name": "Shrii",
        "age": 20
    }
}

print(d["student"]["name"])

# Output:
# Shrii


# =========================================================
# 📌 10. DICTIONARY COMPREHENSION
# =========================================================

d = {x: x*x for x in range(5)}
print(d)

# Output:
# {0:0, 1:1, 2:4, 3:9, 4:16}


# =========================================================
# 📌 11. MERGING DICTIONARIES
# =========================================================

d1 = {"a":1}
d2 = {"b":2}

print({**d1, **d2})

# Output:
# {'a':1, 'b':2}


# =========================================================
# 📌 12. IMPORTANT LOGIC EXAMPLE
# =========================================================

# Frequency counter
lst = [1,2,2,3]

freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1

print(freq)

# Output:
# {1:1, 2:2, 3:1}


# =========================================================
# 📌
# =========================================================

print("Dictionary = Key-Value + Mutable + Unique Keys")

# Output:
# Dictionary = Key-Value + Mutable + Unique Keys