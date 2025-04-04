import cv2
import numpy as np
from numba import cuda
import argparse

@cuda.jit
def to_grayscale_gpu(image, gray):
    x,y = cuda.grid(2)

    if x < image.shape[0] and y < image.shape[1]:
        b,g,r = image[x,y]
        # Manual grayscale conversion using the weights for eye sensitivity
        gray[x,y] = 0.114 * b + 0.587 * g + 0.299 * r



