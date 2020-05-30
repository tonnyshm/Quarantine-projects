import cv2
import sys

# creating dataset for the webcam
cpt = 0
vidstream = cv2.VideoCapture(0)

while True:
    ret, frame = vidstream.read()
    cv2.imshow("Test Frame", frame)
    cv2.imwrite(r"C:\Users\HP\PycharmProjects\face-recognition\images\0\image%04i.jpg" %cpt,frame)
    cpt += 1

    if cv2.waitKey(10) == ord("q"):
        break

