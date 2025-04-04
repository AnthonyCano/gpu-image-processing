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


# If block for the script to be run in the command line

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    # This reads the image and returns it as a OpenCV matrix
    image = cv2.imread(args.input)
    gray = to_grayscale_cpu(image)

    cv2.imshow("Grayscale (CPU)", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

