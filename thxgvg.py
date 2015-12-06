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

if __name__ == "__main__":
    import doctest
    doctest.testmod()