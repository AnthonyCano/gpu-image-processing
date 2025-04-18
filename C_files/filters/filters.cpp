#include "opencv2/core.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "iostream"
#include "filters.hpp"

using namespace cv;
using namespace std;

bool applyGrayscaleFilter(cl_context context,
                          cl_command_queue queue,
                          cl_program program,
                          cl_mem inputImageBuffer,
                          cl_mem outputGrayBuffer,
                          int width,
                          int height){
  String imageName("../images/test.jpg");

}


