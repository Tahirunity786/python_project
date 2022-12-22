# BOOLEAN DATA TYPE WORKOUT

if 10 == 9:
    print("This through a false statement")

if 10 > 9:
    print("This through true statement")

if 10 != 9:
    print("This through false")

if 9 == 9:
    print("This through true")

print(bool("Tahir"))
print(bool(1))
# This is bool value is false
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

#                     BOOLEAN VALUES ARE USE IN MANY CASES
class myClass():
    def __len__(self):
        return 1

myCls = myClass()
print(bool(myCls))

def myFunction():
    return True
myFunction();

print("\n")
def myfunc1():
    return False
def myfuc2():
    return True

if myfunc1():
    print("Your statement is YES")
elif myfuc2():
    print("Your statement is false")
