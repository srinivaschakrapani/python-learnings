class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.link = link


class SLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, info):
        newnode = Node(info)
        if self.head is None:
            self.head = newnode
        else:
            newnode.link = self.head
            self.head = newnode
        print("Node inserted At beginning successfully !!")
        self.printsll()

    def insert_at_end(self, info):
        newnode = Node(info)
        if self.head is None:
            self.head = newnode
        else:
            currnode = self.head
            while currnode.link is not None:
                currnode = currnode.link
            currnode.link = newnode
        print("Node inserted At END successfully !!")
        self.printsll()

    def deletenode(self, info):
        if self.head is None:
            print('No elements to delete')
        else:
            prev = currnode = self.head
            while currnode.link is not None:
                if currnode.info == info:
                    if currnode is self.head:
                        self.head = currnode.link
                        break
                    else:
                        print('Node deleted !!')
                        prev.link = currnode.link
                        break
                prev = currnode
                currnode = currnode.link
        self.printsll()

    def printsll(self):
            currnode = self.head
            while currnode != None:
                print(currnode.info)
                currnode = currnode.link


if __name__ == '__main__':
    # src = [6, 5, 3, 1, 8, 7, 2, 4]
    LL = SLL()
    LL.insert_at_beginning(10)
    LL.insert_at_end(20)
    LL.insert_at_beginning(-1)
    LL.insert_at_end(-2)
    LL.deletenode(20)
    #LL.printsll()
