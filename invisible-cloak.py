import cv2
import numpy as np

cap = cv2.VideoCapture(1)
back = cv2.imread('./image.jpg')

while cap.isOpened():
    # take each frame
    ret, frame = cap.read()

    if ret:
        # how do we convert rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv",hsv)

        # how to get hsv value??
        # lower: hue - 10,100,100, higher: h+10,255,255
        blue = np.uint8([[[255, 0, 0]]])
        hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
        # get hsv value of blue from bgr
        # print(hsv_blue)

        # threshold the hsv value to only get blue colors
        l_blue = np.array([100, 100, 100])
        h_blue = np.array([130, 255, 255])

        mask = cv2.inRange(hsv, l_blue, h_blue)
        # cv2.imshow("mask", mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("mask", part2)

        # cloak = cv2.morphologyEx(part1 + part2, cv2.MORPH_OPEN,kernel=)
        # cv2.imshow("cloak", cloak)
        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
