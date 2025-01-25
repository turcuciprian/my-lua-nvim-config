class Node:
    """A simple Node class for the linked list."""
    
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """A basic LinkedList class with a reverse method."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node to the end of the list."""
        
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        """Reverse the order of nodes in the linked list."""
        
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Update the head reference after reversal
        self.head = prev

    def print_list(self):
        """Print all elements in the linked list."""
        
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original List:")
linked_list.print_list()  # Output: 1 2 3 4

linked_list.reverse()

print("Reversed List:")
linked_list.print_list()  # Output: 4 3 2 1
