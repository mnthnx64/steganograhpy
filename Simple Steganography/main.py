"""
Python program to realize the
simple stenography which implements both 
coding and decoding part.

:Author: Manthan C S
:GitHub: mnthnx64
"""

from coder import Coder
from decoder import Decoder

if __name__ == '__main__':
    cdr = Coder("In all the examples so far, the elements of a are provided by the iterator one at a time, because all the looping logic is internal to the iterator. While this is simple and convenient, it is not very efficient. A better approach is to move the one-dimensional innermost loop into your code, external to the iterator. This way, NumPy’s vectorized operations can be used on larger chunks of the elements being visited.")
    cdr.encode()
    dcdr = Decoder()
    text = dcdr.decode()
    print(text)