# Invisible Cloak

### This is a Image Processing Python Script which helps us create effects like making something invisible when a certain color is placed under it. The libraries used in this project are :-

1. numpy
2. OpenCV

### NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

### OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source Apache 2 License.

<!-- 
#### In this python project, I've used Haar-Cascade-Frontal-Detection Algorithm.

[Haar Cascade Frontal Face XML](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml "Haar Cascade XML") -->

### cv2 uses BGR (blue, gree, red) but in this project we're working with hsv file format, i.e. (hue, saturation, value/brightness).

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

[This](background.py) app uses our web-cam and clicks an image of the background which will act as the base for our invisible cloak file to run on.
It will set the background image over which the resulting masking is performed.

The new file will be saved as background.jpg. 

```python
cv2.imshow("image", back)
if cv2.waitKey(5) == ord("q"):
    # save the image
    cv2.imwrite('background.jpg', back)
    break
```

#### In [this](invisible-cloak.py) project I've used Blue as the color of my cloak. After working with the background image, the low saturation and the high saturation of my color, i.e Blue is set using NumPy arrays.

```python
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
# get hsv value of blue from bgr
# print(hsv_blue)

# threshold the hsv value to only get blue colors
l_blue = np.array([100, 100, 100])
h_blue = np.array([130, 255, 255])
```

#### After the colors are selected, masking is done on the background image and the current webCam image to add all the exisiting colors than blue.

``` python
mask = cv2.inRange(hsv, l_blue, h_blue)
# cv2.imshow("mask", mask)

part1 = cv2.bitwise_and(back, back, mask=mask)
# cv2.imshow("part1", part1)

mask = cv2.bitwise_not(mask)

part2 = cv2.bitwise_and(frame, frame, mask=mask)
```

### Invisible Cloak
![Working GIF of Invisible-Cloak-Project][inv-cloak]

[inv-cloak]: invisible-cloak.gif "Invisible-Cloak-Project"