# Create a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


# Create a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.head is None:
            return ''
        curr_node = self.head
        element = ''
        while curr_node:
            element += f'{curr_node.data} -> '
            curr_node = curr_node.next
        element += 'None'
        return element

    def add(self,element):
        """Add the new element[s] at the end of linkedlist
        
        Time Complexity: O[elements to add]
        Auxiliary Space Complexity: O(1)

        param element: new element to add in linkedlist at the end
        type element: any  
        """
        if type(element) is list:
            for e in element:
                self.add(e)
        else:
            new_node = Node(element)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            self.tail.next = new_node
            self.tail = self.tail.next

    def addleft(self,element):
        """Add the new element[s] at the front of linkedlist
        
        Time Complexity: O(elements to add)
        Auxiliary Space Complexity: O(1)

        param element: new element to add in linkedlist at the front
        type element: any  
        """
        if type(element) is list:
            for e in element:
                self.addleft(e)
        else:
            if not self.head:
                self.head = Node(element)
                self.tail = self.head
            else:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node
    
    def getnode(self, value): 
        """Takes data of a node and returns first occurence of the node 
        reference if the data present at any of the node 
        otherwise returns None

        Time Complexity: O(n)
        Auxiliary Space Complexity: O(1)

        param value: data of a node
        type value: any type

        return: Node reference is the data present otherwise return None 
        """
        curr_node = self.head
        while(curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if(curr_node.data == value):
            return curr_node
        else:
            return None

    def getcount(self):
        """Returns the total number of nodes present in the LinkedList 
        
        Time Complexity: O(n)
        Auxiliary Space Complexity: O(1)
        """
        if self.head is None:
            return 0

        count=1
        curr=self.head
        while(curr.next):
            count+=1
            curr=curr.next
        return count

    def getmid(self):
        """Return the mid Node of LinkedList

        Time Complexity: O(n/2)
        Auxiliary Space Complexity: O(1)
        """
        if(not self.head):   return None
        first = self.head
        second = self.head
        while(second and second.next):
            first = first.next
            second = second.next.next
        return first

    def delete_from_mid(self, node):
        """Take a Node reference and delete it from the LinkedList

        Time Complexity: O(1)
        Auxiliary Space Complexity: O(1)

        param node: Node reference of any node present in the linkedlist
        type node: object of class Node
        """
        if node.next is not None:
            node.data = node.next.data
            node.next = node.next.next
        else:
            node = None


    def insert_at_mid(self,element):
        """Takes a element and add it in the middle of LinkedList

        Time Complexity: O(n/2)
        Auxiliary Space Complexity: O(1)

        param element: object that needs to add in the middle of list
        type element: any type
        """
        node = Node(element)
        if not self.head.next:
            self.head.next = node
            return
        
        prev = None
        first=self.head
        second=self.head
        while second and second.next:
            prev = first
            first = first.next
            second = second.next.next
        
        if not second:
            prev.next = node
            node.next = first
        elif not second.next:
            next = first.next
            first.next = node
            node.next = next

    def at(self, index):
        """Take the position as parameter and the data available at that
        position and if the position is greater than the length of list
        return None

        Time Complexity: O(n)
        Auxiliary Space Complexity: O(1)

        param index: position of Node
        type: int
        """
        curr=self.head
        count=1
        while(curr and count!=index):
            count+=1
            curr=curr.next
        return curr.data if curr else None
