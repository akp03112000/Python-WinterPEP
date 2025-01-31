Class
Node
def_int_(Self)
Self
data = data
Self.next = None
Class
Stack:
def_init_(Self)
Self.head = None


def push(Self, data)
    if Self.head == none
        Self.head = Node(data)
    else:
        new_node = Node(data)


new_node.next = Self.head
Self.head = new_node


def pop(Self)
    if Self top == None
    return ("not possible")
    else:
    top = Self.top
    Self.top = Self.top.next

tempNext = None