#!/usr/local/bin/python3
small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')
def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    result = []
    result.append(title.split()[0].capitalize())
    for i in title.split()[1:]:
        if i.lower() not in small_words:
            result.append(i.capitalize())
        else:
            result.append(i.lower())
    return print("'{0}'".format(" ".join(result)))

def _test():
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
