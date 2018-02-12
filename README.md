# cloudFind
Highlights clouds yellow

# PURPOSE: 

Identify parts of sky which are clear and cloudy. The clouds ranging from white
to grey are identified and coloured in yellow.

# USE: 

To run the program in cmd/terminal type:<b> python find-cloud.py images/*.jpg </b>
or <b> python find-cloud.py image.jpg </b>

# PROGRAM: 

Takes image input and is stored as BGR pixels by OpenCV, which is converted to
HSV from BGR. The HSV image pixel values are passed to hsvCheck function and
stored in numpy array(data).  The array(data) is looped through to take each
HSV pixel, of which the hue, saturation and brighness are taken from the pixel
value. Then the program checks for saturation less than 41 and brightness more
than 35, to find the grey shades. if the pixel values matchs the set condition,
then the pixel value of BGR image is changed to yellow. After the whole image
processing is completed, the edited image and original image is shown using
numpy stack and OpenCV imshow.

# RESTRICTIONS

Need to use MacOS or Linux, with <b> Python 2 </b> and <b> OpenCV 3 </b> installed.
<i> Images need to contain grey-white clouds within sky. </i>
