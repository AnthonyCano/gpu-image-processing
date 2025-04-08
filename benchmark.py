import time
import cv2
from filters.grayscale_cpu import to_grayscale_cpu
from filters.grayscale_gpu_numba import apply_gpu_filter

image = cv2.imread("images/test.jpg")

# CPU 
start = time.perf_counter()
cpu_result = to_grayscale_cpu(image)
end = time.perf_counter()
print(f"CPU Time: {(end -start) * 1000:.2} ms")

# GPU
start = time.perf_counter()
gpu_result = apply_gpu_filter(image)
end = time.perf_counter()
print(f"GPU Time: {(end - start) * 1000:.2f} ms")
