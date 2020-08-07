class Node:
    def __init__(self,info, prev=None, nxt=None):
        self.info = info
        self.prev = prev
        self.nxt = nxt

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self, info):
        newnode = Node(info)
        if self.head is None:
            self.head = newnode
        else:
            currnode = self.head
            while currnode.nxt is not None:
                currnode = currnode.nxt
            currnode.nxt = newnode
            newnode.prev = currnode
        print('Node inserted')
        self.print_dll()

    def delete(self, info):
        if self.head is None:
            print('Nothing to delete ')
            return
        else:
            prevnode = currnode = self.head
            if currnode.nxt is None:
                self.head = None
                return
            else:
                while currnode.nxt is not None:
                    if currnode.info == info:
                        prevnode.nxt = currnode.nxt
                        currnode.nxt.prev = prevnode
                        print('Deleted Node')
                        self.print_dll()
                    prevnode = currnode
                    currnode = currnode.nxt

    def print_dll(self):
        currnode = self.head
        while currnode is not None:
            print(currnode.info)
            currnode = currnode.nxt

if __name__ == '__main__':
    # src = [6, 5, 3, 1, 8, 7, 2, 4]
    LL = DLL()
    #LL.insert_at_beginning(10)
    LL.insert_at_end(20)
    #LL.insert_at_beginning(-1)
    LL.insert_at_end(-2)
    LL.insert_at_end(10)
    LL.insert_at_end(20)
    LL.delete(10)
    #LL.deletenode(20)
    #LL.printsll()