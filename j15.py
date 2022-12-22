# This file is based on the comprehension of List

My_list = []

new_list = []

# for i in range(100):
#     if i%3==0:
#         My_list.append(i)
#     elif i%2==0:
#         new_list.append(i)

# print(My_list)
# print(new_list)

#                           COMPREHENSION FORMAT
# new_list = [i for i in range(12) if i%3==0]
# print(new_list)

My_list = [var for var in range(10) if var % 2 == 0]
print(My_list)

new_list = [p for p in My_list if p != 6]
print(My_list)
# simple iteraton
My_list = [var for var in range(10)]
# Lower condition
My_list = [var for var in range(10) if var < 5]
# The use of funtion string in comprehension
My_list2 = ["Tahir", "Zaman", "Usman", "Ali"]

My = [x.upper() for x in My_list2]
print(My)