import cv2 
import argparse

def to_grayscale_cpu(image):
    '''
    Function to take a color image and converts it into
    grayscale. 

    image: image to be converted

    returns: grayscaled image 
    '''
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

