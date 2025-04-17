#ifndef  filters.hpp
#define filters.hpp

#include <CL/cl.h>

bool applyGrayscaleFilter(cl_context context,
                          cl_command_queue queue,
                          cl_program program,
                          cl_mem inputImageBuffer,
                          cl_mem outputGrayBuffer,
                          int width,
                          int height);
#endif 
