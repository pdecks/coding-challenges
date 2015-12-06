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
            node_list.append(current)
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
            self.append_node(node_list.pop().data)
        
        return

def make_anagram_dict(words):
    """Return dictionary mapping sorted letters to list of words with those chars
        
        >>> make_anagram_dict(["act", "cat", "dog", "mouse", "god"])
        {'emosu': ['mouse'], 'dgo': ['dog', 'god'], 'act': ['act', 'cat']}
    """
    anagram_dict = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        anagram_dict.setdefault(sorted_word, []).append(word)

    return anagram_dict


def find_most_anagrams_from_wordlist(wordlist):
    """Given a list of words, return the word with the most anagrams.

    For a list of ['act', 'cat', 'bill']:
    - 'act' and 'cat' are anagrams, so they both have 2 matching words.
    - 'bill' has no anagrams, os it has one matching word (itself).

    Given that 'act' is the first instance of the most-anagrammed word,
    we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

    Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'
    """
    # note, I first tried to solve this with an ordered dict and permutations,
    # but the runtime on that was ridiculous. Much faster to solve with sorted
    # word

    # create a dictionary of anagrams
    anagrams_dict = make_anagram_dict(wordlist)

    # create variables to keep track of make value
    highest_num_anagrams = 0
    most_anagrams = None

    # for each word in wordlist, check if sorted word in anagrams_dict
    for word in wordlist:
        sorted_word = "".join(sorted(word))
        # get the number of words for that key
        number_anagrams = len(anagrams_dict[sorted_word])
        # compare against current max
        if number_anagrams > highest_num_anagrams:
            highest_num_anagrams = number_anagrams
            most_anagrams = word

    return most_anagrams



class TNode(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.

        Let's make this chart:

            >>> henri = TNode("Henri")
            >>> nora = TNode("Nora", [henri])
            >>> nick = TNode("Nick")
            >>> janet = TNode("Janet", [nick, nora])
            >>> al = TNode("Al")
            >>> bob = TNode("Bob")
            >>> jen = TNode("Jen")
            >>> jessica = TNode("Jessica", [al, bob, jen])
            >>> jane = TNode("Jane", [jessica, janet])

        And test our counting function:

            >>> henri.count_employees()
            0

            >>> nora.count_employees()
            1

            >>> jane.count_employees()
            8
        """
        # find the person in the tree
        to_visit = [self]

        ch_count = 0
        while to_visit:
            emp = to_visit.pop()
            for child in emp.children:
                ch_count += 1
                to_visit.append(child)
            
        return ch_count


    def __repr__(self):
        return "<TNode %s>" % self.name


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"

    # my_list = ['apple', 'berry', 'cherry']
    my_list = [1, 2, 3, 4, 5]
    my_LL = LL()
    for item in my_list:
        my_LL.append_node(item)
    print "Printing Linked List ..."
    my_LL.print_LL()
    my_LL.reverse_LL()
    print "Printing Reversed Linked List ..."
    my_LL.print_LL()

