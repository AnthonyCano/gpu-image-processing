import time
import cv2
from filters.grayscale_cpu import to_grayscale_cpu
from filters.grayscale_gpu_numba import to_grayscale_gpu

image = cv2.imread("images/test.jpg")

# CPU 
start = time.perf_counter()
cpu_result = to_grayscale_cpu(image)
end = time.perf_counter()


