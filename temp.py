from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

frame = cv2.imread('thor.jpg')

arr = np.array(frame)

rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

plt.imshow(rgb)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces = classifier.detectMultiScale(frame)

face = faces[0]

x, y, w, h = face

face = rgb[y:y+h, x:x+w]

out = cv2.rectangle(rgb, (x,y), (x+w,y+h),(255,0,0),2)

cv2.imwrite('image1.jpg', out)

plt.imshow(out)