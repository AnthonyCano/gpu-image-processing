import cv2
import numpy as np
from numba import cuda
import argparse

@cuda.jit
def to_grayscale_gpu(image, gray):
    '''
    Function to convert image to grayscale using the GPU.
    Uses manual grayscale conversion using weights that
    are within the human eye color filter range.

    Inputs
    image: The image to be converted to grayscale
    gray: The opencv matrix created from converting to grayscale
    '''
    x,y = cuda.grid(2)

    if x < image.shape[0] and y < image.shape[1]:
        b,g,r = image[x,y]
        # Manual grayscale conversion using the weights for eye sensitivity
        gray[x,y] = 0.114 * b + 0.587 * g + 0.299 * r

def apply_gpu_filter(image):
    img_device = cuda.to_device(image)
    gray_device = cuda.device_array((image.shape[0], image.shape[1]), dtype=np.uint8)

    threadsperblock = (16, 16)
    blockspergrid_x = (image.shape[0] + threadsperblock[0] - 1) // threadsperblock[0]
    blockspergrid_y = (image.shape[1] + threadsperblock[1] - 1) // threadsperblock[1]
    to_grayscale_gpu[(blockspergrid_x, blockspergrid_y), threadsperblock](img_device, gray_device)

    return gray_device.copy_to_host()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    image = cv2.imread(args.input)
    gray = apply_gpu_filter(image)

    cv2.imshow("Grayscale (GPU)", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
