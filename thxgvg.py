def is_palindrome(somestr):
    """Return True if string somestr is a palindrome.

        >>> is_palindrome("a")
        True

        >>> is_palindrome("noon")
        True

        >>> is_palindrome("racecar")
        True

        >>> is_palindrome("porcupine")
        False

        >>> is_palindrome("Racecar")
        False
    """
    # number of steps required at most (len(somestr) / 2)
    for i in range(len(somestr)):
        other = len(somestr) - i - 1
        if somestr[i] != somestr[other]:
            return False
    return True


def is_prime(num):
    """Return True if integer num is a prime number.

        >>> is_prime(0)
        False

        >>> is_prime(1)
        False

        >>> is_prime(2)
        True

        >>> is_prime(3)
        True

        >>> is_prime(4)
        False

        >>> is_prime(11)
        True

        >>> is_prime(999)
        False
    """
    # a prime number >= 2
    if num < 2:
        return False

    # if mod any number larger than 2 but smaller than the number == 0
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    Given the numbers 1-10, return n random numbers, making sure to never return
    the same number twice. You can trust that this function will never be called
    with n < 0 or n > 10.

        # >>> lucky_numbers(2)
        # [3, 7]

        >>> lucky_numbers(0)
        []

        >>> sorted(lucky_numbers(10))
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    if n == 0:
        return []
    
    import random
    nums = list(xrange(1, 11))
    lucky_nums = []

    i = 0
    while i < n:
        value = random.choice(nums)
        nums.remove(value)
        lucky_nums.append(value)
        i += 1

    return lucky_nums


def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    Check edge cases of empty lists:

        >>> sort_ab([], [])
        []

        >>> sort_ab([1, 2,3], [])
        [1, 2, 3]

        >>> sort_ab([], [1, 2, 3])
        [1, 2, 3]

    Check:

        >>> sort_ab([1, 3, 5, 7], [2, 6, 8, 10])
        [1, 2, 3, 5, 6, 7, 8, 10]
    """
    # initialize new, empty list for results
    merged_list = []

    # compare first element of each sorted list until one of them is empty
    while len(a) > 0 or len(b) > 0:
        # append the remaining items from the non-empty list to results list
        if a == []:
            merged_list.append(b.pop(0))
        elif b == []:
            merged_list.append(a.pop(0))
        # remove whichever is lower and add it to the results
        elif a[0] < b[0]:
            merged_list.append(a.pop(0))
        else:
            merged_list.append(b.pop(0))

    return merged_list


class Node(object):
    """Nodes for a linked list"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

        return


class LL(object):
    """Linked list of nodes"""

    def __init__(self):
        self.head = None
        self.tail = None
        return


    def append_node(self, data):
        """Add node with data to end of list."""
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

        return


    def print_LL(self):
        """Print all items in the linked list"""
        current = self.head

        while current is not None:
            print current.data
            current = current.next
        return


    def traverse_LL(self):
        """Traverse a linked list and return list of nodes"""
        current = self.head
        node_list = []
        while current is not None:
            node_list.append(current.data)
            current = current.next

        return node_list


    def reverse_LL(self):
        """Takes the head node of a linked list and returns the head of a new,
        reversed linked list."""
        # traverse the LL to find the end, simultaneously storing nodes in a stack
        node_list = self.traverse_LL()
        
        # at the end, move head to end
        self.head = node_list.pop()

        # pop items off stack into new LL
        while node_list:
            self.append_node(node_list.pop())
        
        return


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    my_list = [1, 2, 3, 4, 5]
    my_LL = LL()
    for item in my_list:
        my_LL.append_node(item)
    my_LL.print_LL()
    my_LL.reverse_LL()
    my_LL.print_LL()

