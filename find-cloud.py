#!/usr/bin/env python
#------------------------------------------------------------------------------
# PURPOSE: 
'''
Identify parts of sky which are clear and cloudy. The clouds ranging from white
to grey are identified and coloured in yellow.
'''
# USE: 
'''
To run the program in cmd/terminal type: python find-cloud.py cloudpix/*.jpg
or python find-cloud.py image.jpg
'''
# PROGRAM: 
'''
Takes image input and is stored as BGR pixels by OpenCV, which is converted to
HSV from BGR. The HSV image pixel values are passed to hsvCheck function and
stored in numpy array(data).  The array(data) is looped through to take each
HSV pixel, of which the hue, saturation and brighness are taken from the pixel
value. Then the program checks for saturation less than 41 and brightness more
than 35, to find the grey shades. if the pixel values matchs the set condition,
then the pixel value of BGR image is changed to yellow. After the whole image
processing is completed, the edited image and original image is shown using
numpy stack and OpenCV imshow.
'''
# CODE DEFINITIONS:
'''
-cv2.cvtColor: change defualt BGR to GREYSCALE or HSV.
-numpy.copy: copies array
-numpy.asarray: input data in any form and convert to an array.
-numpy.hstack: stacks array in sequence horizontally.
-cv2.imshow: display image in a window
'''
#MODIFY
'''
Modifying the code is not recommended, but if wishes to make changes to 
find grey levels, a basic level of HSV knowledge is required and in line 68,
the user may change the saturation and brightness condition values and may add
hue to the condition, which is already declared in the line above.
'''
#RESTRICTIONS
'''
Need to use MacOS or Linux, with Python 2 and OpenCV 3 installed.
Images need to contain grey-white clouds within sky.
'''
# REFERENCES:
'''
Summarize.py lecture python code by Dr Adrian Clark
https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/ :Show
two images side by side
#http://colorizer.org/ :Used to work out grey values of RGB and HSV
'''
#------------------------------------------------------------------------------
import sys, cv2, numpy, pylab

#------------------------------------------------------------------------------
# Routines.
#------------------------------------------------------------------------------

# Processing image to find grey pixels
def hsvCheck(img, hsv):
    # store HSV pixels in array
    data = numpy.asarray(hsv)
        
    # BGR pixels to yellow if saturation and brightness condition is true
    for i in range(len(data)):
        for j in range(len(data[0])):
            hue,saturation,brightness = data[i,j]
            if saturation <= 41 and brightness > 35:
               img[i,j] = [0,255,255]

#------------------------------------------------------------------------------
# Main program.
#------------------------------------------------------------------------------

# Ensure the command line is sensible.
if len (sys.argv) < 2:
    print >>sys.stderr, "Usage:", sys.argv[0], "<image>..."
    sys.exit (1)

# Process and show the files given on the command line.
for fn in sys.argv[1:]:
    # Read image, make copy of image and convert to HSV and pass HSV image to
    # hsvCheck to process
    im = cv2.imread (fn)
    imy = numpy.copy(im)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    hsvCheck(im, hsv)

    # Display copied image and edited image for 2 seconds
    cv2.imshow (fn, numpy.hstack([im,imy]))
    cv2.moveWindow(fn, 0,0)
    cv2.waitKey (2000)
    cv2.destroyWindow (fn)

#------------------------------------------------------------------------------
# END OF find-cloud.py 
#------------------------------------------------------------------------------
