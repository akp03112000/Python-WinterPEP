class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def length(self):

            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            return count

    def display(self):

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

linked_list.display()


print("Length of linked list:", linked_list.length())