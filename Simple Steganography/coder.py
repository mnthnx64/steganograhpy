"""
Python program to realize the
coding part of stenography.

:Author: Manthan C S
:GitHub: mnthnx64
"""
import cv2
import numpy as np
import math

class Coder:
    """
    Encodes a string into an image using 
    basic addition logic of ascii values.

    :functions: encode()
    """

    base_image = None
    ascii_char = list()

    def __init__(self, text):
        """
        initializes the Coder class with
        the supplied text and creates the
        base image.

        :return: None
        """
        for char in str(text):
            self.ascii_char.append(ord(char))
        self._img_shape = math.floor(math.sqrt(len(self.ascii_char)))+1
        self.base_image = np.zeros((1,512), dtype=np.uint8)
        # Uncomment the below line to get a precise bounded image         
        # self.base_image = np.zeros((1,self._img_shape), dtype=np.uint8) 

    def encode(self):
        """
        Contains logic to add the 
        ascii values to the base image and 
        saves it.

        :return: Saves an image
        """
        count = len(self.ascii_char)
        with np.nditer(self.base_image, op_flags=['readwrite']) as iteratable:
            for i,element in enumerate(iteratable):
                if count !=0:
                    element[...] = element + self.ascii_char[i]
                    count -= 1
                else:
                    break
        
        self.base_image = np.tile(self.base_image, (512,1))
        # Uncomment the below line to get a precise bounded image 
        # self.base_image = np.tile(self.base_image, (self._img_shape,1))

        cv2.imwrite('coded.png', self.base_image)

# x = Coder('The nditer will then yield writeable buffer arrays which you may modify. However, because the nditer must copy this buffer data back to the original array once iteration is finished, you must signal when the iteration is ended, by one of two methods')
# x.encode()