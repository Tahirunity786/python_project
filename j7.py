# This file is based in the string formatting
# This is done through some function

a = "My name is Tahir Zaman"
b = 19
# print("My name is Tahir Zaman" + 19) this is an error through statement, Because str is not concatenate with integer
# This is done through format function
a = "My name is Tahir Zaman, I'm {} years old"
#  {} is must
print(a.format(b))
# Some example
quantity = 3
item = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."
print(my_order.format(quantity, item, price))
