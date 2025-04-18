#ifndef FILTERS_HPP
#define FILTERS_HPP

#include <CL/cl.h>
#include <opencv2/opencv.hpp>
#include <string>

// Initializes OpenCL context, device, and builds program from .cl file
bool initOpenCL(cl_context& context,
    cl_command_queue& queue,
    cl_program& program,
    const std::string& kernelFilePath);

// Applies the grayscale filter using OpenCL
bool applyGrayscaleFilter(cl_context context,
                          cl_command_queue queue,
                          cl_program program,
                          cl_mem inputImageBuffer,
                          cl_mem outputGrayBuffer,
                          int width,
                          int height);
#endif // FILTERS_HPP
