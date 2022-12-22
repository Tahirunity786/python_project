#                                                       THIS FILE IS BASED ON THE SORT OF STRING
# This will include string sorting in list
# This will include number sorting in list

#                                                       String sorting in list

my_list = ["Tahir", "Zaman", "Ali", "Ahmad", "Noman"]

my_list.sort()
print(my_list)

my_list = ["Tahir", "Zaman", "Ali", "Ahmad", "Noman"]

my_list.sort(reverse=True)
print(my_list)
for i in my_list:
    print(i)

my_list_2 = [1, 2, 3, 10, 5.8, 11, 7, 99, 9, 10]
my_list_2.sort()
print(my_list_2)

my_list_2 = [1, 2, 3, 10, 5.8, 11, 7, 99, 9, 10]
my_list_2.sort(reverse=True)

print(my_list_2)
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
# Sorted and sort in Python is That sort() [orignal change the list directly] and no return but the sorted() no change directly and returnd a value
def myf(n):
  return n[1]

my_list_3 = [[12, 13], [14, 15], [16, 0], [89, -1], [0.1,4]]
my_list_3.sort(key=myf)
print(my_list_3)
