#                                          This is file is based on list modification
# This first step belong
Mylist1 = [12, 13, 14, 15, 16, 17]

# The list is based on index
# The list is start from 0
# print(Mylist1[0])
# print(Mylist1[1])
# print(Mylist1[2])
# print(Mylist1[3])
# print(Mylist1[4])

# The list can also access through back tracing
print(Mylist1[-6:])
# SPECIFIC SEARCHING
mylist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist2[2:5])
# UNKNOWN START
MYLIST3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(MYLIST3[:4])
# UNKNOWN end
MYLIST4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(MYLIST4[2:])

MYLIST5 = ["apple", "banana", "cherry"]
if "apple" in MYLIST5:
    print("Yes, 'apple' is in the fruits list")
