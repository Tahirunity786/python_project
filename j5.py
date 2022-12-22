# STRING DECLARING
# Single line string declaring
str1 = "Hello! My name is Tahir Zaman, I'm student of Software Engineering"
# print(str1)
# This is Many line declare string
str2 = """Hello! My name is Tahir Zaman, I'm student of Software Engineering, I have started my degree journey in 
2021, Ins-hallah, I'll passed my exams with high percentage number. 
"""
# print(str2)
# Important to know that string is a collection of array
# WE can access with array
# for i in str1:
#     print(i)

# String slicing concept is an important concept of Python
# we know that string in an array collection
# We can print specific number os string with the help of string slicing

# we can find the length of string with the help of 'len()' function

# Before going to this process method we see some str technique

a = "This is string"
# Print specific
# print(a[0])
# Print with loop
# for i in a:
#     print(i)
#
# # Print the length
# print("\n")
# print(len(a))
# string searching

# if "is" in a:
#     print("is has found\n")
# elif "is" not in a:
#     print("not found")
# else:
#     print("Try again")

# string slicing concept has started
# we have a variable contain some string
# contain a variable and store sliced string init
Tahir_variable = a[0:4]
Tahir_variable_2 = a[5:7]
Tahir_variable_3 = a[8:14]
print(Tahir_variable+"\n"+Tahir_variable_2+"\n"+Tahir_variable_3+"\n")

# Starting with unknown start
Tahir_variable_4 = a[:6]
Tahir_variable_5 = a[:10]
Tahir_variable_6 = a[:14]
print(Tahir_variable_4+"\n"+Tahir_variable_5+"\n"+Tahir_variable_6)

# specific to specific
Tahir_variable_7 = a[4:10]
Tahir_variable_8 = a[3:12]
Tahir_variable_9 = a[1:10]
print(Tahir_variable_7+"\n"+Tahir_variable_8+"\n"+Tahir_variable_9+"\n")

# Reverse slicing
print("Reverse slicing has started")
Tahir_variable_10 = a[-4:-1]
print(Tahir_variable_10)
print("\n")
Tahir_variable_11 = a[-10:-5]
print(Tahir_variable_11)
print("\n")
Tahir_variable_12 = a[-14:-10]
print(Tahir_variable_12)
print("\n")

# unknown
Tahir_variable_4 = a[:6]
Tahir_variable_5 = a[:10]
Tahir_variable_6 = a[:14]
