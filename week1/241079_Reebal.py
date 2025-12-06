import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

#Defining custom function to show images while comparing

def print_image(original,image):

    plt.figure(figsize=(20,10))

    plt.subplot(1,2,1)
    plt.imshow(original)
    plt.title("Original Picture")
    plt.xticks(list(range(0,1001,100)))
    plt.yticks(list(range(0,1201,100)))
    plt.axis('on')
   
   
    plt.subplot(1,2,2)
    plt.imshow(image,cmap='gray')
    plt.title("Picture Boundaries")
    plt.xticks(list(range(0,1001,100)))
    plt.yticks(list(range(0,1201,100)))
    plt.axis('on')

    plt.tight_layout()
    plt.show()



#Reading image

original=cv2.imread("mario.png")

#Converting from BGR to RGB for imshow() to read
original= cv2.cvtColor(original, cv2.COLOR_BGR2RGB)

image=cv2.imread("mario.png")


#Converting to grayscale

image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Using canny output

canny_output=cv2.Canny(image,50,180)



print_image(original,canny_output)



