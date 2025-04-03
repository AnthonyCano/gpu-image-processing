This project demonstrates how to accelerate image processing operations using GPU computation. Built with Python and GPU tools like Numba or OpenCL. Benchmarks GPU vs. CPU performance and shows the power of parallel processing.

---

## Features

- Load and display images with OpenCV
- Apply common filters:
  - Grayscale
  - Edge Detection (Sobel)
  - Gaussian Blur
- GPU-accelerated filter execution (Numba or OpenCL)
- Side-by-side CPU vs GPU performance benchmarking
- CLI or GUI (coming soon!)

---

### Dependencies

- Python 3.8+
- GPU-compatible device (NVIDIA or Intel)
- pip (Python package manager)

### Installation

```bash
git clone https://github.com/anthonycano/gpu-image-processing.git
cd gpu-image-processing
pip install -r requirements.txt
