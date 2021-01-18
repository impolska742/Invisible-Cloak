import cv2

# THIS IS MY WEBCAM
cap = cv2.VideoCapture(1)

while cap.isOpened():

    # HERE I'M JUST READING FROM MY WEBCAM
    ret, back = cap.read()
    # ret : return number to check if it is working fine.

    if ret:
        # back : what camera is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord("q"):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
