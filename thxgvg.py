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


if __name__ == "__main__":
    import doctest
    doctest.testmod()