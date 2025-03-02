---
title: OpenCV Imaging
parent: Python notes
layout: default
nav_order: 6
---

# OpenCV (Compputer Vision)
{: .no_toc }

- TOC
{:toc} 

Install the opencv-contrib-python and numpy libraries:

```
pip install opencv-contrib-python numpy
```

OpenCV is a sophisticated image processing library. It takes considerably more disk space than Pillow so use that if you don't need the features of OpenCV. OpenCV is used with machine learning computer vision tasks such as face detection/recognition and object detection/recognition.

Sample code recipes

Use the camera, display the video frames and save to PNG

```py
import cv2
import numpy as np

capture = cv2.VideoCapture(0)       # Camera number
capture.set(3, 800)                 # Request camera width
capture.set(4, 600)                 # Request camera height
while True:
    ret, img = capture.read()       # Get image from camera
    cv2.imshow('window label',img)  # Show on screen
    k = cv2.waitKey(100)            # Wait 100 ms for keypress
    if k % 256 == 27:               # If ESC key pressed
        break
cv2.imwrite("final-frame.png", img) # Save final frame as a PNG
```

Use the camera, save video file.

```py
capture = cv2.VideoCapture(0)           # Camera number
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video=cv2.VideoWriter('video.mp4',fourcc,25,(800,600))
while True:
    ret, img = capture.read()           # Get success code and image from camera
    frame = cv2.resize(img, (800,600))  # Resize image to 800x600
    video.write(frame)                  # Add frame to video
    k = cv2.waitKey(100)                # Wait 100 ms for keypress
    if k % 256 == 27:                   # If ESC key pressed
        break
video.release()                         # Close video file when done
```
 
Basic face detection

Requires the cascade file (contains the pattern information to detect a face) from [https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

```py
import cv2
import numpy as np
yellow = (0,255,255)                # Yellow in BGR colors
n = 0                               # Number of faces seen
capture = cv2.VideoCapture(0)       # Camera number
capture.set(3, 800)                 # Request camera width
capture.set(4, 600)                 # Request camera height
cascade_file = "imagestuff\haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascade_file)
while True:
    status, img = capture.read()       # Get success code and image from camera
    # By default image is BGR (Blue Green Red) rather than RGB
    # Create gray scale image for face detection algorithm to use
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect any faces in the image? Put coordinates of any faces seen in an array
    faces = cascade.detectMultiScale(
        gray,               # Use the grayscale image
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(100, 100)  # Minimum pixel size to recognise as a "face"
    )
    # For every face we found
    for (x,y,w,h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x,y), (x+w,y+h), yellow, 2)
        face = img[y:y+h, x:x+w]            # Extract the face portion of the image
        cv2.imwrite(f"face-{n}.png", face)  # Save the face image to disk
        n = n + 1
    cv2.imshow('window label',img)          # Show on screen
    k = cv2.waitKey(100)                    # Wait 100 ms for keypress
    if k % 256 == 27:                       # If ESC key pressed
        break
cv2.imwrite("final-frame.png", img) # Save final frame as a PNG
```

### Commonly used functions

Read an image file

```py
# Returns numpy array, containing the pixel values. For colored images, each pixel is represented as an array containing Red, Green and Blue and optionally Alpha channels.
img = cv2.imread("image.png")
```

Read a video file

```py
video = cv2.VideoCapture("video.mp4")
```

Read a video stream from camera

```py
# Read a video stream from camera
video = cv2.VideoCapture(0) # parameter = camera number
```

Read an image (frame) from the video file or camera

```py
status, image = video.read()
```

Get information about the image (for colour images)

```py
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2] # Will not exist for grayscale
```

Get an individual pixel

```py
pixel = img[y, x]
```

Resize an image

```py
img2 = cv2.resize(img, (800,600))
```

Overlay text onto an image
* Parameters of the putText() function: image, string message, top/left coordinates, font scale, color, font width.

```py
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Message", (x,y), 1, yellow, 2)
```

Display an image on screen

```py
cv2.imshow('window label',img)
```

Convert colour modes

```py
# Image conversions - examples
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # From BGR to grayscale
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # From BGR to RGB
bgr = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)      # From RGBA to BGR
```

Convert PIL image object to CV2 numpy array

```py
cv2_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
```

Convert CV2 numpy array to PIL image object

```py
pil_image = Image.fromarray(cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB))
```

Paste one image onto another

```py
h,w,channels = img2.shape   # Get dimensions of img2 to paste
x, y=50,50                  # Coordinates to apply paste in img1
img1[y:y+h, x:x+w] = img2   # Will paste without regard to alpha transparency
cv2.imshow("Final product",img1)
```
