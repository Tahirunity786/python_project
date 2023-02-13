
class Node:
    def __init__(self, data):
        self.name = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def append(self, Employee, id):
        New_Node = Node({'Name': Employee, 'ID': id})
        if self.head is None:
            self.head = New_Node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = New_Node

    def Print_list(self):
        temp = self.head
        while temp:
            print(temp.name)
            temp = temp.next


List_Object = Linked()
List_Object.append("Tahir", 1)
List_Object.append("Tahir", 22800)
List_Object.append("Tahir", 800)
List_Object.append("Tahir", 20800)
List_Object.append("Tahir", 30800)
List_Object.Print_list()
