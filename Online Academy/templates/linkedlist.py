#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        current = self.head
        end = self.tail
        new_node = Node(item)

        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node



    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)
        self.head = new_node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        node = Node(item)
        current = self.head
        if current != None:
            if current.data==item:
                temp = current.next
                del current
                self.head = temp

                if self.head == None:
                    self.tail = None
            else:
                  current = self.head
                  print(current)
                  while current.next.data != item:
                      current = current.next
                  print(item)
                  temp = current.next.next
                  del current.next
                  current.next = temp
                  print(temp)
                  if current.next is None:

                      if self.tail.data == item:

                          self.tail = current
        else:
              raise ValueError('Item not found: {}'.format(item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""

        current = self.head
        if quality is current.data:
            return current.data
        current = current.next
        return None



def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    # print(ll.length())
    print('About to run delete function')
    # ll.delete('A')

    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # ll.delete('C')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # ll.delete('B')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    ll.delete('D')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    # print(ll.length())


if __name__ == '__main__':
    test_linked_list()
