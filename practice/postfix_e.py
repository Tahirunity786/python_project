
def isopr(operator):
    if operator == '+':
        return True
    if operator == '-':
        return True
    if operator == '*':
        return True
    if operator == '^':
        return True
    if operator == '/':
        return True
    else:
        return False


def Application(My_String):
    mylist = []
    lenght_of_string = len(My_String)
    for i in range(lenght_of_string):
        if isopr(My_String[i]):
            str1 = mylist[-1]
            mylist.pop()
            str2 = mylist[-1]
            mylist.pop()

            main_str = My_String[i]+str2+str1

            mylist.append(main_str)
        else:
            mylist.append(My_String[i])
    ans = ""
    for i in mylist:
        ans += i

    return ans


if __name__ == "__main__":

    post_fix_value = "Zaman+/*-1235Z-*"

    print(Application(post_fix_value))
