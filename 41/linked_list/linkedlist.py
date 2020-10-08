class LinkedList:
    def __init__(self):
        self.head = None
        self.__nrOfNodes = 0

    def __add__(self, data):
        if self.head == None:
            self.head = Node(data)
            self.__nrOfNodes += 1
        else:
            currentNode = self.head
            while(currentNode.next != None):
                currentNode = currentNode.next
            currentNode.next = Node(data)
            self.__nrOfNodes += 1

    def append(self, data):
        self.__add__(data)

    def clear(self):
        self.head = None

    def __contains__(self, data):
        currentNode = self.head
        while(currentNode != None):
            if currentNode.data == data:
                return True
            currentNode = currentNode.next
        return False

    def copy(self):
        pass

    def count(self, data):
        pass

    def __delitem__(self, position):
        pass

    def extend(self, iterable):
        pass

    def __getitem__(self, position):
        pass

    def index(self, index):
        pass

    def insert(self, position, element):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __mul__(self, multiples):
        pass

    def __imul__(self, multiples):
        pass

    def __rmul__(self, multiples):
        pass

    def pop(self, optionalPosition = 0):
        pass

    def remove(self, element):
        pass

    def reverse(self):
        pass

    def __reversed__(self):
        pass

    def __setitem__(self, position, element):
        pass

    def sort(optionalKey = '', optionalReverseBool = False):
        pass

    def __repr__(self):
        if self.head == None:
            return 'list empty'
        else:
            tempList = []
            currentNode = self.head
            while(currentNode != None):
                tempList.append(currentNode.data)
                currentNode = currentNode.next
            return str(tempList)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

l = LinkedList()
l + 'hey'
