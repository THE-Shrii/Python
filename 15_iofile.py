# # =========================================================
# # 🐍 PYTHON FILE I/O
# # =========================================================
#
#
# # =========================================================
# # 📌 1. WHAT IS FILE I/O?
# # =========================================================
#
# # File I/O = Reading and Writing data to files
# # Used for permanent storage
#
#
# # =========================================================
# # 📌 2. OPENING A FILE
# # =========================================================
#
# # Syntax:
# # file = open("filename", "mode")
#
# f = open("demo.txt", "r")   # read mode
#
#
# # =========================================================
# # 📌 3. FILE MODES
# # =========================================================
#
# # "r"  → Read (default)
# # "w"  → Write (overwrite)
# # "a"  → Append
# # "x"  → Create new file
# # "b"  → Binary mode
# # "t"  → Text mode (default)
#
# # Examples:
# # open("file.txt", "r")
# # open("file.txt", "w")
# # open("file.txt", "a")
#
#
# # =========================================================
# # 📌 4. READING FILE
# # =========================================================
#
# # read() → reads full content
# f = open("demo.txt", "r")
# print(f.read())
# f.close()
#
# # readline() → reads one line
# f = open("demo.txt", "r")
# print(f.readline())
# f.close()
#
# # readlines() → returns list of lines
# f = open("demo.txt", "r")
# print(f.readlines())
# f.close()
#
#
# # =========================================================
# # 📌 5. WRITING FILE
# # =========================================================
#
# # write() → overwrite content
f = open("demo.txt", "w")
f.write("Hello Shrii")
f.close()
#
# # Output: File content becomes "Hello Shrii"
#
#
# # =========================================================
# # 📌 6. APPENDING FILE
# # =========================================================
#
# f = open("demo.txt", "a")
# f.write("\nNew Line Added")
# f.close()
#
# # Output:
# # Hello World
# # New Line Added
#
#
# # =========================================================
# # 📌 7. WITH STATEMENT (BEST PRACTICE)
# # =========================================================
#
# # Automatically closes file
#
# with open("demo.txt", "r") as f:
#     print(f.read())
#
#
# # =========================================================
# # 📌 8. IMPORTANT METHODS
# # =========================================================
#
# f = open("demo.txt", "r")
#
# # tell() → current position
# print(f.tell())
#
# # seek() → move cursor
# f.seek(0)
#
# # readable()
# print(f.readable())
#
# # writable()
# print(f.writable())
#
# f.close()
#
#
# # =========================================================
# # 📌 9. FILE EXIST CHECK
# # =========================================================
#
# import os
#
# if os.path.exists("demo.txt"):
#     print("File exists")
#
#
# # =========================================================
# # 📌 10. DELETE FILE
# # =========================================================
#
# import os
#
# os.remove("demo.txt")
#
#
# # =========================================================
# # 📌 11. COPY FILE
# # =========================================================
#
# with open("demo.txt", "r") as f1:
#     with open("copy.txt", "w") as f2:
#         f2.write(f1.read())
#
#
# # =========================================================
# # 📌 12. BINARY FILE
# # =========================================================
#
# # Example: image or pdf
# f = open("image.jpg", "rb")
# data = f.read()
# f.close()
#
#
# # =========================================================
# # 🎯 END OF FILE I/O
# # =========================================================