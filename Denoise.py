# importing libraries
import numpy as np
import os
import cv2
from matplotlib import pyplot as plt

# Reading image from folder where it is stored
class Denoise:
    def test(a,b):
        print(a)
        print(b)
        img = cv2.imread(a)
        img2 = cv2.imread(b)
        
        # denoising of image saving it into dst image
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        dst2 = cv2.fastNlMeansDenoisingColored(img2, None, 10, 10, 7, 15)

        #Plotting of source and destination image
        # plt.subplot(121)
        plt.imsave(a,dst)
        # plt.subplot(122) 
        plt.imsave(b,dst2)
        # plt.show()