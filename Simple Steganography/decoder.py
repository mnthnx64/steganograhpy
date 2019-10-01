"""
Python program to realize the
decoding part of stenography.

:Author: Manthan C S
:GitHub: mnthnx64
"""
import cv2
import numpy as np

class Decoder:
    """
    Decodes a stenographic image back into text using 
    basic subtraction logic of ascii values.

    :functions: decode()
    """
    text = list()
    
    def __init__(self):
        """
        Initializes the decoder class
        Reades the coded image and gets
        the coded part

        :return: None
        """
        image = cv2.imread('coded.png', 0)
        self.coded_part = image[0]

    def decode(self):
        """
        Deodes the encrypted image 
        back into text.

        :return: str(Decoded Text)
        """
        for av in self.coded_part:
            if av!=0: self.text.append(chr(av))
        final = ''.join(self.text)
        return final

# x = Decoder()
# x.decode()