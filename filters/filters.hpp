#ifndef FILTERS_HPP
#define FILTERS_HPP

#include <CL/cl.h>

bool applyGrayscaleFilter(cl_context context,
                          cl_command_queue queue,
                          cl_program program,
                          cl_mem inputImageBuffer,
                          cl_mem outputGrayBuffer,
                          int width,
                          int height);
#endif // FILTERS_HPP
